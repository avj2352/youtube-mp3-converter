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

- [Updating Metadata using Python's eyed3 library](https://stackoverflow.com/questions/8948/accessing-mp3-metadata-with-python)
- [Youtube to MP3 converter python script](https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/)
- [Intro to Pytube - Freecodecamp](https://www.freecodecamp.org/news/python-program-to-download-youtube-videos/)
- [Youtube DL tutorial](https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/)
- [Convert Audio .wav to .mp3 using ffmpeg](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)
- [Youtube DL python script](https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py)
- [Youtube to MP3 using nodejs](http://pauldbergeron.com/articles/streaming-youtube-to-mp3-audio-in-nodejs.html)
- [Medium - convert .wav to .mp3](https://devtails.medium.com/how-to-convert-audio-from-wav-to-mp3-in-node-js-using-ffmpeg-e5cb4af2da6)

## Instructions - using uv

- Create a folder to save mp3 files - `download`
- From the root folder, run `uv run main.py`

## Instructions - using pip

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


## PytubeFix - 10/03/25

- Github link: [https://github.com/JuanBindez/pytubefix/issues/542](Github issue)
- Title: `pytubefix.exceptions.RegexMatchError: get_initial_function_name: could not find match for multiple in https://youtube.com/s/player/377ca75b/player_ias.vflset/en_US/base.js #542`


```bash
@NannoSilver and @felipeucelli many thanks. i am terrible with git. how do i install felipeucelli@ca8c67f?

i did: pip install "pytubefix @ git+https://github.com/felipeucelli/pytubefix.git@ca8c67f"

tested it but instead of receiving usual output (the title of a video i own) i am getting some kind log that ends with a broken pipe

i know it is a newbe question....
pip install --upgrade --force-reinstall --no-cache-dir git+https://github.com/felipeucelli/pytubefix.git@sig-nsig
```

UV command to for the above pip command

```bash
uv pip install --reinstall --no-cache git+https://github.com/felipeucelli/pytubefix.git@sig-nsig
```
