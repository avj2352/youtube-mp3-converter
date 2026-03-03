# PDF to Audiobook using Google Gemini 2.5 Pro TTS

Here's a complete Python script that converts a PDF into an audiobook using Google's Gemini 2.5 Pro with text-to-speech capabilities.

## Prerequisites

First, install the required packages:

```bash
pip install google-genai PyPDF2 pydub
```

## Complete Code

```python
"""
PDF to Audiobook Converter using Google Gemini 2.5 Pro TTS
==========================================================
Converts a PDF file into an audiobook (WAV/MP3) using Google's
Gemini 2.5 Pro model with native text-to-speech output.
"""

import argparse
import io
import struct
import sys
import wave
from pathlib import Path

from google import genai
from google.genai import types
from PyPDF2 import PdfReader


# ──────────────────────────────────────────────
#  Configuration
# ──────────────────────────────────────────────
GEMINI_MODEL = "gemini-2.5-pro-preview-tts"
DEFAULT_VOICE = "Kore"          # Options: Aoede, Charon, Fenrir, Kore, Puck, etc.
SAMPLE_RATE = 24000             # Gemini outputs 24 kHz audio
CHANNELS = 1                    # Mono
SAMPLE_WIDTH = 2                # 16-bit PCM (2 bytes)
MAX_CHARS_PER_CHUNK = 4000      # Max characters per TTS request (to stay within limits)


# ──────────────────────────────────────────────
#  1. Extract Text from PDF
# ──────────────────────────────────────────────
def extract_text_from_pdf(pdf_path: str) -> str:
    """Read all pages of a PDF and return the combined text."""
    reader = PdfReader(pdf_path)
    all_text = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            all_text.append(text.strip())
        print(f"  📄 Extracted page {i + 1}/{len(reader.pages)}")
    return "\n\n".join(all_text)


# ──────────────────────────────────────────────
#  2. Chunk the Text
# ──────────────────────────────────────────────
def chunk_text(text: str, max_chars: int = MAX_CHARS_PER_CHUNK) -> list[str]:
    """
    Split text into chunks that respect sentence boundaries.
    Each chunk will be ≤ max_chars characters.
    """
    sentences = []
    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        # Naive sentence splitting — works for most prose
        for sent in paragraph.replace(". ", ".|").split("|"):
            sent = sent.strip()
            if sent:
                sentences.append(sent)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # If a single sentence exceeds the limit, force-split it
        if len(sentence) > max_chars:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""
            for j in range(0, len(sentence), max_chars):
                chunks.append(sentence[j : j + max_chars])
            continue

        if len(current_chunk) + len(sentence) + 1 > max_chars:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            current_chunk += " " + sentence if current_chunk else sentence

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


# ──────────────────────────────────────────────
#  3. Convert Text Chunk → Audio via Gemini TTS
# ──────────────────────────────────────────────
def synthesize_speech(
    client: genai.Client,
    text: str,
    voice: str = DEFAULT_VOICE,
) -> bytes:
    """
    Send a text chunk to Gemini 2.5 Pro TTS and return raw PCM audio bytes.
    """
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice,
                    )
                )
            ),
        ),
    )

    # The response contains inline audio data
    audio_data = response.candidates[0].content.parts[0].inline_data.data
    return audio_data


# ──────────────────────────────────────────────
#  4. Combine Audio Chunks → WAV File
# ──────────────────────────────────────────────
def save_wav(pcm_chunks: list[bytes], output_path: str):
    """Combine raw PCM audio chunks into a single WAV file."""
    with wave.open(output_path, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(SAMPLE_WIDTH)
        wf.setframerate(SAMPLE_RATE)
        for chunk in pcm_chunks:
            wf.writeframes(chunk)
    print(f"\n✅ WAV file saved: {output_path}")


def convert_wav_to_mp3(wav_path: str, mp3_path: str):
    """Optionally convert WAV → MP3 using pydub (requires ffmpeg)."""
    try:
        from pydub import AudioSegment
        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3", bitrate="192k")
        print(f"✅ MP3 file saved: {mp3_path}")
    except Exception as e:
        print(f"⚠️  MP3 conversion failed (is ffmpeg installed?): {e}")


# ──────────────────────────────────────────────
#  5. Main Pipeline
# ──────────────────────────────────────────────
def pdf_to_audiobook(
    pdf_path: str,
    output_path: str = "audiobook.wav",
    api_key: str | None = None,
    voice: str = DEFAULT_VOICE,
    export_mp3: bool = True,
):
    """
    Full pipeline: PDF → Text → Chunks → TTS → Audio File.
    
    Args:
        pdf_path:    Path to the input PDF file.
        output_path: Path for the output WAV file.
        api_key:     Google AI API key (or set GOOGLE_API_KEY env var).
        voice:       TTS voice name.
        export_mp3:  Also export an MP3 version.
    """
    # ── Validate input ──
    if not Path(pdf_path).exists():
        print(f"❌ File not found: {pdf_path}")
        sys.exit(1)

    # ── Initialize Gemini client ──
    client = genai.Client(api_key=api_key)  # Uses GOOGLE_API_KEY env var if None
    print(f"🔑 Gemini client initialized (model: {GEMINI_MODEL})")

    # ── Step 1: Extract text ──
    print(f"\n📖 Extracting text from: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    if not text.strip():
        print("❌ No text found in the PDF.")
        sys.exit(1)
    print(f"   Total characters extracted: {len(text):,}")

    # ── Step 2: Chunk text ──
    chunks = chunk_text(text)
    print(f"\n🔪 Split into {len(chunks)} chunk(s) for TTS processing")

    # ── Step 3: Synthesize each chunk ──
    audio_chunks: list[bytes] = []
    for i, chunk in enumerate(chunks):
        print(f"\n🎙️  Synthesizing chunk {i + 1}/{len(chunks)} "
              f"({len(chunk)} chars)...")
        try:
            pcm_data = synthesize_speech(client, chunk, voice=voice)
            audio_chunks.append(pcm_data)
            print(f"   ✓ Received {len(pcm_data):,} bytes of audio")
        except Exception as e:
            print(f"   ✗ Error on chunk {i + 1}: {e}")
            # Insert a short silence so the audiobook doesn't skip
            silence_duration = 1  # seconds
            silence = b"\x00" * (SAMPLE_RATE * SAMPLE_WIDTH * CHANNELS * silence_duration)
            audio_chunks.append(silence)

    # ── Step 4: Save combined audio ──
    print(f"\n📼 Combining {len(audio_chunks)} audio segments...")
    save_wav(audio_chunks, output_path)

    # ── Optional: MP3 export ──
    if export_mp3:
        mp3_path = str(Path(output_path).with_suffix(".mp3"))
        convert_wav_to_mp3(output_path, mp3_path)

    print("\n🎉 Audiobook generation complete!")


# ──────────────────────────────────────────────
#  CLI Entry Point
# ──────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a PDF into an audiobook using Google Gemini 2.5 Pro TTS"
    )
    parser.add_argument("pdf", help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output",
        default="audiobook.wav",
        help="Output WAV file path (default: audiobook.wav)",
    )
    parser.add_argument(
        "-k", "--api-key",
        default=None,
        help="Google AI API key (or set GOOGLE_API_KEY env var)",
    )
    parser.add_argument(
        "-v", "--voice",
        default=DEFAULT_VOICE,
        help=f"TTS voice name (default: {DEFAULT_VOICE})",
    )
    parser.add_argument(
        "--no-mp3",
        action="store_true",
        help="Skip MP3 conversion",
    )

    args = parser.parse_args()

    pdf_to_audiobook(
        pdf_path=args.pdf,
        output_path=args.output,
        api_key=args.api_key,
        voice=args.voice,
        export_mp3=not args.no_mp3,
    )
```

## Usage

### Command Line

```bash
# Set your API key (get one from https://aistudio.google.com/apikey)
export GOOGLE_API_KEY="your-api-key-here"

# Basic usage
python pdf_to_audiobook.py mybook.pdf

# Custom output, voice, and skip MP3
python pdf_to_audiobook.py mybook.pdf -o my_audiobook.wav -v Puck --no-mp3

# Pass API key directly
python pdf_to_audiobook.py mybook.pdf -k "AIza..."
```

### As a Python Module

```python
from pdf_to_audiobook import pdf_to_audiobook

pdf_to_audiobook(
    pdf_path="mybook.pdf",
    output_path="mybook_audio.wav",
    api_key="AIza...",
    voice="Kore",
    export_mp3=True,
)
```

## Available Voices

| Voice | Description |
|-------|-------------|
| `Kore` | Warm, female (default) |
| `Puck` | Upbeat, male |
| `Charon` | Deep, authoritative |
| `Fenrir` | Calm, male |
| `Aoede` | Bright, female |

> See the full list in the [Gemini TTS docs](https://ai.google.dev/gemini-api/docs/text-generation#voice).

## How It Works

```
┌─────────┐     ┌──────────────┐     ┌─────────────┐     ┌───────────────┐
│  PDF     │────▶│ Text Extract │────▶│  Chunk Text │────▶│ Gemini 2.5    │
│  File    │     │  (PyPDF2)    │     │  (≤4000 ch) │     │ Pro TTS API   │
└─────────┘     └──────────────┘     └─────────────┘     └───────┬───────┘
                                                                  │
                                                          PCM audio bytes
                                                                  │
                                                          ┌───────▼───────┐
                                                          │  Combine &    │
                                                          │  Save WAV/MP3 │
                                                          └───────────────┘
```

**Pipeline Steps:**

1. **PDF Text Extraction** — `PyPDF2` reads every page and extracts text
2. **Sentence-Aware Chunking** — Text is split into ≤4,000 character chunks at sentence boundaries to respect API limits
3. **TTS Synthesis** — Each chunk is sent to `gemini-2.5-pro-preview-tts` with `response_modalities=["AUDIO"]`, returning raw PCM audio
4. **Audio Assembly** — All PCM chunks are concatenated and written as a WAV file (24 kHz, 16-bit, mono), with optional MP3 export via `pydub`/`ffmpeg`

## Notes

- **API Key**: Get one free at [Google AI Studio](https://aistudio.google.com/apikey)
- **Rate Limits**: The script processes chunks sequentially. For very large PDFs, you may hit rate limits — consider adding `time.sleep()` between chunks
- **MP3 Export**: Requires `ffmpeg` installed on your system (`brew install ffmpeg` / `apt install ffmpeg`)
- **Scanned PDFs**: This only works with text-based PDFs. For scanned/image PDFs, you'd need OCR (e.g., `pytesseract`) first
