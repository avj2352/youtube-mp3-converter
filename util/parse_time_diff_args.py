'''
Update convert input output files for ffmpeg
'''
from os.path import isfile
from typing import List
import getopt, sys, os
import logging

arg_list = sys.argv[1:]

# command line arguments
options = "s:e:"
# long options
long_options = ["start=", "end="]
value_map = {}


def parse_time_args() -> dict:
    try:
        arguments, _ = getopt.getopt(arg_list, options, long_options)
        # check each argument present
        for curr_arg, curr_value in arguments:
            if curr_arg in ("-s", "--start"):
                value_map['start'] = curr_value
            if curr_arg in ("-e", "--end"):
                 value_map['end'] = curr_value
        logging.debug(f"Value list is: {str(value_map)}")
    except getopt.error as err:
        logging.error(str(err))
    return value_map

# FOR TESTING
if __name__ == "__main__":
    parse_time_args()

