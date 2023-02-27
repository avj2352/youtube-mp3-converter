'''
Update MP3 file with media artwork

'''
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import logging

# @deprecated
def update_artwork(files: dict): 
    mp3file=files.get('music')
    audio = MP3(mp3file, ID3=ID3)
    image_data = open(files.get('art'),'rb').read()
    try:
        audio.add_tags()
    except Exception as err:
        logging.debug(f"No need to create: ${str(err)}")
    audio.tags.add(
        APIC(
            encoding=1,
            mime='image/png',
            type=3,
            desc=u'Cover',
            data=image_data
            )
        )
    audio.save()
