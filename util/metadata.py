'''
Python library to add metadata information to MP3 file
'''
import logging
from eyed3 import load


def update_metadata(meta: dict = {}):
    logging.debug(f"Media file: {meta.get('file')}")
    try:
        file_path = meta.get('file', None)
        # guard
        if not file_path:
            logging.debug(f"No Media file")
            return
        audio = load(file_path)
        if audio.tag is None:
            audio.initTag()
        audio.tag.artist = meta.get('artist', '')
        audio.tag.album = meta.get('album', '')
        audio.tag.title = meta.get('title', '')
        audio.tag.genre = meta.get('genre', '')
        audio.tag.track_num = 1
        audio.tag.save()
        logging.debug('Updated metadata...!')
    except Exception as err:
        logging.debug(str(err))
