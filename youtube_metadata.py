'''
Update mp3 metadata using eyed3 lib
'''
from util.artwork import update_artwork
from util.parse_eyed3_args import parse_eyed3_options
from util.metadata import update_metadata
import logging
import os


# api related
API_LOGGING_LEVEL=os.environ.get('API_LOGGING_LEVEL') or "DEBUG"

# logging config
logging.basicConfig(
        level=API_LOGGING_LEVEL,
        format="%(asctime)s ~%(filename)s~ %(levelname)s:- %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")


def add_artwork(files: dict):
    # check if media artwork file is present
    if not files or not files.get('art'):
        logging.debug(f"No artwork file found, Skipping Artwork update")
        return
    # logging.debug(f"MP3 and artwork files: {str(files)}")
    update_artwork(files)

def add_metadata(files: dict):
    meta = {
            'file': files.get('music'),
            'title': '',
            'artist': '',
            'album': '',
            'genre': 'Soundtrack'
            }
    title = input("Enter Title (skip): ")
    artist = input("Enter Artist name (skip): ")
    album = input("Enter Album name (default: \"\"): ")
    genre = input("Enter Genre (default: \"Soundtrack\"): ")
    
    meta['title'] = title if title != '' else ''
    meta['artist'] = artist if artist != '' else ''
    meta['album'] = album if album != '' else ''
    meta['genre'] = genre if genre != '' else 'Soundtrack'
    # logging.debug(f"Configuring metadata...{str(meta)}")
    update_metadata(meta)

def main():
    files: dict = parse_eyed3_options()
    # edge case
    if not files or not files.get('music'):
        logging.debug(f"No mp3 file found, Try again")
        return
    # add metadata
    add_metadata(files)
    # add artwork
    add_artwork(files) 


# FOR TESTING
if __name__ == "__main__":
    main()
    

