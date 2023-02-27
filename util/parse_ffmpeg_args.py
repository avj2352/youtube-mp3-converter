'''
Update convert input output files for ffmpeg
'''
from os.path import isfile
from typing import List
import getopt, sys, os
import logging

arg_list = sys.argv[1:]

# command line arguments
options = "s:d:"
# long options
long_options = ["src=", "dest="]
value_map = {}


def parse_ffmpeg_options() -> dict:
    try:
        arguments, _ = getopt.getopt(arg_list, options, long_options)
        # check each argument present
        for curr_arg, curr_value in arguments:
            if curr_arg in ("-s", "--src"):
                if os.path.isfile(curr_value):
                    value_map['src'] = curr_value
                else:
                    logging.error('Wrong src path entered, try again!')
                # logging.debug(f"Music path is {curr_value}")
            if curr_arg in ("-d", "--dest"):
                if curr_value.endswith('mp3'):
                    value_map['dest'] = curr_value
                else:
                    logging.error('Wrong artfile path entered')
                # logging.debug(f"Art path is {curr_value}")
        # logging.debug(f"Value list is: {str(value_map)}")
    except getopt.error as err:
        logging.error(str(err))

    return value_map

# FOR TESTING
if __name__ == "__main__":
    parse_options()

