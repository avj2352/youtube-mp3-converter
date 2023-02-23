# Youtube Downloader

## Important Links
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
youtube-dl -x --audio-format mp3 'https://www.youtube.com/watch?v=ND5snVy4Fnw'
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
