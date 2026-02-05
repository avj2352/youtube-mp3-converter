# Youtube MP3 Toolsuite

Simple CLI application to download, convert to MP3 format, and add metadata information.
Metadata information include
- Title
- Artist
- Album Artist
- Genre
- Album Artwork

> You need `ffmpeg` encoder installed in your machine in order for the following scripts to work

- youtube_converter.py
- youtube_metadata.py

## Important Links

- [PytubeFix Github repo link](https://github.com/JuanBindez/pytubefix)
- [Updating Metadata using Python's eyed3 library](https://stackoverflow.com/questions/8948/accessing-mp3-metadata-with-python)
- [Youtube to MP3 converter python script](https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/)
- [Intro to Pytube - Freecodecamp](https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/)
- [Youtube DL tutorial](https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/)
- [Convert Audio .wav to .mp3 using ffmpeg](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)
- [Youtube DL python script](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py)
- [Youtube to MP3 using nodejs](http://pauldbergeron.com/articles/streaming-youtube-to-mp3-audio-in-nodejs.html)
- [Medium - convert .wav to .mp3](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)

## Instructions

Below is a comprehensive list of all Python script files in your project, including their overview and how to run them using both uv and standard Python
commands.

### 1. youtube_converter.py or main.py

**Overview:** Converts audio/video files to MP3 format using ffmpeg. Requires source and destination file paths as command-line arguments. Uses the libmp3lame codec with
quality scale settings.

```bash
# Using uv
uv run youtube_converter.py 

# Using standard Python
python youtube_converter.py 
# or
python3 youtube_converter.py -s <source_path> -d <destination_path>

# Arguments:

# • -s - Source file path
# • -d - Destination file path
```
### 2. youtube_playlist_download.py

**Overview:** Downloads an entire YouTube playlist as audio files using the pytubefix library. Prompts the user for a playlist URL and downloads all videos in audio-only
format.

```bash
# Using uv
uv run youtube_playlist_download.py

# Using standard Python
python youtube_playlist_download.py
# or
python3 youtube_playlist_download.py
```

### 3. opus_convert.py

**Overview:** Converts Opus audio files to MP3 format using ffmpeg. Can be used as a module or run standalone for testing. The script prompts for the input Opus file
location and desired output MP3 filename.

```bash
# Using uv
uv run opus_convert.py

# Using standard Python
python opus_convert.py
# or
python3 opus_convert.py

```

### 4. combine_audio.py

**Overview:** Combines multiple M4A audio files into a single MP3 file using ffmpeg. Supports custom output filenames, bitrate selection, and verbose output. Can process
specified files or all M4A files in the current directory.

```bash
# Using uv - with specific files
uv run combine_audio.py \
file1.m4a \
file2.m4a \
-o output.mp3

# Using uv - all M4A files in current directory
uv run combine_audio.py -o output.mp3

# Using uv - with custom bitrate
uv run combine_audio.py file1.m4a file2.m4a -o output.mp3 -b 320k

# Using standard Python
python combine_audio.py file1.m4a file2.m4a -o output.mp3
# or
python3 combine_audio.py -h  # for help
```

### 5. rename_camelcase.py

**Overview:** Renames files to camelCase format while preserving file extensions. Handles special characters, apostrophes, hyphens, and can optionally remove parenthetical
content. Supports dry-run mode to preview changes before applying them.

```bash
# Using uv - basic usage
uv run rename_camelcase.py "My File.mp3" "Another File.txt"

# Using uv - dry run (preview only)
uv run rename_camelcase.py -d *.m4a

# Using uv - remove parenthetical content
uv run rename_camelcase.py -r "Track (01).m4a"

# Using uv - run tests
uv run rename_camelcase.py -t

# Using standard Python
python rename_camelcase.py file1.txt "My File.mp3"
# or
python3 rename_camelcase.py -d *.m4a

```

### 6. mp3_metadata.py

**Overview:** Identifies and displays MP3 file encoding parameters including bitrate, sample rate, channels, length, and bitrate mode (CBR vs VBR). Currently hardcoded to
check a specific file path (requires modification for general use).

```bash
# Using uv
uv run mp3_metadata.py

# Using standard Python
python mp3_metadata.py
# or
python3 mp3_metadata.py

# Note: Edit the script to change the hardcoded file path: ./download/xmen_movie_themes_soundtrack.mp3
```
### 7. youtube_metadata.py

**Overview:** Updates MP3 metadata tags (title, artist, album, genre) and optionally adds album artwork. Prompts the user interactively for metadata values and uses helper
utilities for artwork and metadata management.

```bash
# Using uv - with MP3 file only
uv run youtube_metadata.py -m ./download/song.mp3

# Using uv - with MP3 file and artwork
uv run youtube_metadata.py -m ./download/song.mp3 -a ./download/artwork.jpeg

# Using standard Python
python youtube_metadata.py -m ./download/song.mp3 -a ./download/artwork.jpeg
# or
python3 youtube_metadata.py -m <mp3_file> -a <artwork_file>

# Arguments:

# • -m - Path to the MP3 file (required)
# • -a - Path to the artwork file (optional)
```
---

## How to - use uv

- Create a folder to save mp3 files - `download`
- From the root folder, run `uv run main.py`

## How to - use pip

- Clone / Download the ZIP version into your local machine
- Create  folder to save mp3 files - `download`
- Setup a Local environment using `python -m venv venv --prompt="utump3(3.11)"`
- Activate the virtual environment

```bash
  # For Macbook
  source ./venv/Scripts/activate

  # For windows
  ./venv/Scripts/activate.bat
```

- Run the following to install dependant libraries

```python
pip install -r requirements.txt
```

## TLDR;

Read more about the error in the link below
-[NoneType object has no attribute span](https://github.com/pytube/pytube/issues/1498)

I just patched this error by simply modifying venv/.local/lib/python3.7/site-packages/pytube/cipher.py Line 411

```python
transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)
```
to
```python
transform_plan_raw = js

```
And everything works fine. Hope this can solve your problem.
Thank you very much! It worked perfectly here. 
I have no idea how this change fixed the bug (if you want to explain that would be great), but it worked perfectly anyway.


## Youtube Converter

You need to convert the downloaded file to an `Actual` MP3 audio file. Run the following script from terminal

```bash
# s - source path (source location of the media file)
# d - destination path (where you want the converted file to reside)
python3 ./youtube_converter.py -s ./download/harry_potter.mp3 -d ./download/harry_potter_convert.mp3
```

## Youtube Metadata

In order to add metadata information (including artwork file) run the following script from terminal

```bash
# m - path to the mp3 file
# a - path to the artwork file (optional)
python3 ./youtube_metadata.py -m ./download/harry_potter_ea_games_soundtrack_convert.mp3 -a ./download/harry_potter.jpeg
```

## Combine Audio Script

To run `combine_audio.py` find the example below

```bash
uv run combine_audio.py \
./download/file.m4a \
./download/file_02.m4a \
-o ./download/soundtrack.mp3
```


## PytubeFix - 10/03/25

- Github link: [https://github.com/JuanBindez/pytubefix/issues/542](Github issue)
- Title: `pytubefix.exceptions.RegexMatchError: get_initial_function_name: could not find match for multiple in https://youtube.com/s/player/377ca75b/player_ias.vflset/en_US/base.js #542`


```bash
@NannoSilver and @felipeucelli many thanks. i am terrible with git. how do i install felipeucelli@ca8c67f?

i did: pip install "pytubefix @ git+https://github.com/felipeucelli/pytubefix.git@ca8c67f"

tested it but instead of receiving usual output (the title of a video i own) i am getting some kind log that ends with a broken pipe

i know it is a newbie question....
pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/felipeucelli/pytubefix.git@sig-nsig
```

UV command to for the above pip command

```bash
uv pip install --reinstall --no-cache git+https://github.com/felipeucelli/pytubefix.git@sig-nsig
```
