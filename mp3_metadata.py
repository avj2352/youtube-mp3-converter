"""
    Python script to identify
    file's encoding parameters
"""

from mutagen.mp3 import MP3
from mutagen.id3 import ID3

audio = MP3("./download/xmen_movie_themes_soundtrack.mp3")
print(f"Bitrate: {audio.info.bitrate}")
print(f"Sample rate: {audio.info.sample_rate}")
print(f"Channels: {audio.info.channels}")
print(f"Length: {audio.info.length} seconds")
print(f"Bitrate mode: {audio.info.bitrate_mode}")  # CBR vs VBR
