# Youtube MP3 Toolsuite

You need `ffmpeg` encoder installed in your machine in order for this Python script to work

## Instructions - using uv

- From the root folder, run `uv run main.py`

## Instructions - using pip

- Clone / Download the ZIP version into your local machine
- Setup a Local environment using `python -m venv venv`
- Activate the local environment

## TLDR;

```bash
  # For Macbook
  source ./venv/Scripts/activate

  # For windows
  ./venv/Scripts/activate.bat
```
- Run pip install by reading of requirements.txt file
```bash
pip install -r requirements.txt
```


## ERROR! 
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


## Important Links
- [Updating Metadata using Python's eyed3 library](https://stackoverflow.com/questions/8948/accessing-mp3-metadata-with-python)
- [Youtube to MP3 converter python script](https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/)
- [Intro to Pytube - Freecodecamp](https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/)
- [Youtube DL tutorial](https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/)
- [Convert Audio .wav to .mp3 using ffmpeg](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)
- [Youtube DL python script](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py)
- [Youtube to MP3 using nodejs](http://pauldbergeron.com/articles/streaming-youtube-to-mp3-audio-in-nodejs.html)
- [Medium - convert .wav to .mp3](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)

Simple CLI application to download, convert to MP3 format, and add metadata information.
Metadata information include
- Title
- Artist
- Album Artist
- Genre
- Album Artwork


## Pre-requisite

Tested on both windows and linux. You need to have the following installed

- Clone the project, Setup `venv`
- Activate your virtual environment

```bash
# on windows
./venv/scripts/activate

# on linux/mac
source ./venv/scripts/Activate

```
- Run the following to install dependant libraries

```python
pip install -r requirements.txt
```
- Also python being a general purpose programming language, cannot convert media files into mp3 format. You need to install `ffmpeg` audio-encoder library and have it's executable registered in the path environment variable. You can do this on windows easily using `choco install ffmpeg`, choco  will install and set the path requirements. On Macbook, use `brew install ffmpeg`.


## Youtube Downloader

To download from youtube, run the `./youtube_download.py` script using Python

```bash
# on linux
python3 ./youtube_download.py
# on windows
python ./youtube_download.py
```

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
