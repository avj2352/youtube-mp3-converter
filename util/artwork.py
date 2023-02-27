import eyed3

from eyed3.id3.frames import ImageFrame
import mimetypes
import logging

def update_artwork(files: dict):
    audiofile = eyed3.load(files.get('music'))
    file_type = mimetypes.guess_type(files.get('art'))
    mp3_type = mimetypes.guess_type(files.get('music'))
    # logging.debug(f"Artwork file: {files.get('art')}")
    logging.debug(f'MP3 File type: {mp3_type[0]}')
    logging.debug(f'Artwork File type: {file_type[0]}')
    if audiofile.tag is None:
        audiofile.initTag()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(files.get('art'), 'rb').read(), str(file_type[0]))
    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
