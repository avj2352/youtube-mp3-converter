'''
Update MP3 file with media artwork
'''
from eyed3 import load
import os
import logging
import mimetypes
# from pydub import AudioSegment

def update_artwork(files: dict):
    logging.debug(f"Reading mp3 file: ${files.get('music')}")
    logging.debug(f"Mime type of the file: {mimetypes.guess_type(files.get('music'))}")
    file_type = mimetypes.guess_type(files.get('music'))
    # sound_file = AudioSegment.from_file(files.get('music'))
    # sound_file.export('./download/file.mp3', format="mp3", bitrate="128k")
    # audio_path = './download/file.mp3'
    try:
        picture_path = files.get('art', '')
        audio_path = files.get('music', None)
        # guard
        if not audio_path or not picture_path:
            return
        if not os.path.exists(audio_path):
            logging.debug(f"File does not exist")
            return
        audio = load(audio_path)
        if not audio.tag:
            audio.initTag()
        if not audio.tag or not audio.tag.images: 
            return
        cover_art = open(picture_path, "rb").read()
        audio.tag.images.set(3, cover_art, "image/jpeg")
        audio.tag.save()
    except Exception as err:
        logging.debug(str(err))
