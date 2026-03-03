'''
Download youtube videos as mp3
https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/
'''
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
#..custom
from to_snake_case import to_snake_case 

def Download(link: str):
    print(f"Downloading youtube URL: {link}...")
    youtubeObject = YouTube(link, on_progress_callback=on_progress, use_oauth=True, allow_oauth_cache=True)
    # extract audio
    video = youtubeObject.streams.filter(only_audio=True).first()        
    try:
        if video is None:
            raise ValueError(f"Unable to obtain videa instance from Youtube")
        # download the file
        audio_file = video.download(output_path="./download")
        if audio_file is None:
            raise ValueError("no data when trying to download video")
        base, _ = os.path.splitext(audio_file)
        mp3_file = base + '.mp3'
        os.rename(audio_file, mp3_file)
        print(f"Download has been completed: {video.title}")
        new_file_name: str = to_snake_case(video.title)
        print(f"Renaming file from {video.title} -> {new_file_name}")
        os.rename(mp3_file, f'./download/{new_file_name}.mp3')
    except Exception as e:
        print(f"Error occured: \n {format(e)}")

link = input("Enter youtube URL: ")
Download(link) if link !='' else print("Enter valid URL!")
