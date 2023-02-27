# Youtube MP3 Toolsuite

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

## Important Links
- [Updating Metadata using Python's eyed3 library](https://stackoverflow.com/questions/8948/accessing-mp3-metadata-with-python)
- [Youtube to MP3 converter python script](https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/)
- [Intro to Pytube - Freecodecamp](https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/)
- [Youtube DL tutorial](https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/)
- [Convert Audio .wav to .mp3 using ffmpeg](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)
- [Youtube DL python script](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py)
A Python executable script to download youtube videos online, even convert them to MP3 songs.

## Install

```bash
# deprecated, no need to install brew cask
brew install youtube-dl

# Just run python script
python3 ./youtube_download.py
```

## Convert youtube links to MP3

- NOTE: You need `ffmpeg` to be able to convert

```bash
# script 01
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=MSzOcQWJNUY'

# script 02
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch? ev=ND5snVy4Fnw'
```

# NodeJS - Youtube URL to mp3 converter

## Important Links
- [Medium - convert .wav to .mp3](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)
- [Youtube to MP3 using nodejs](http://pauldbergeron.com/articles/streaming-youtube-to-mp3-audio-in-nodejs.html)


youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=_Ogfr-CTzR8'

youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=TqOVpiXfq0o'

# Matrix - Clubbed to death
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=3W7-WBUhPQU'

# Mandalorian
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=qbMExOE-rDw'

### Mandalorian low-fi music (30 mins)
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=GJEb6jOM07s'

### The Last Kingdom
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=eQHNTHZCCvk'

### Up soundtrack - 20 mins
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=mMUq-MjXJ9M'

### Up Piano - relax
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=1036ZAStqf8'

### Mandalorian - Best soundtracks
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=PkYeErKoDEU'


### Prey - Naru's Theme (extended)
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=DU-it7EALg0'

### Oblivion Suitesound (extended)
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=uf39PoE6bD8'

### Hogwarts Legacy - Suitesound (extended)
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=rTg_36mgo3g'

