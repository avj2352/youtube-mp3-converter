'''
Python itself cannot convert any file to MP3 format 
since it's a file format that requires audio encoding, 
and Python doesn't come with built-in audio encoding capabilities. 
However, you can use third-party libraries in Python to convert audio files to MP3 format.

One popular library for audio encoding in Python is called FFmpeg. 
FFmpeg is a command-line tool that can be used to convert 
audio and video files to various formats, including MP3. 
You can use the subprocess module in Python to execute FFmpeg commands.
'''
import logging
import subprocess
from util.parse_ffmpeg_args import parse_ffmpeg_options

def main():
    files: dict = parse_ffmpeg_options()
    logging.debug(f'src and destination paths: {str(files)}')
    # edge case
    if not files or not files.get('src') or not files.get('dest'):
        logging.error(f"src and dest path not found, Try again")
        return
    input_file = files.get('src')
    output_file = files.get('dest')
    # execute the FFmpeg command to convert the input file to MP3 format
    subprocess.call(["ffmpeg", "-i", input_file, "-codec:a", "libmp3lame", "-qscale:a", "2", output_file])

if __name__ == '__main__':
    main()
