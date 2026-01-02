"""
    Python script to download entire
    playlist into audio files using pytubefix
"""
from pytubefix import Playlist
from pytubefix.cli import on_progress


url = input("Enter the URL of Youtube Playlist: ")
url = url.strip()

print(f"Downloading playlist...")

pl = Playlist(url)
for video in pl.videos:
    ys = video.streams.get_audio_only()
    ys.download()

print(f"Download completed!")
