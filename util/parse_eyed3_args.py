'''
Update mp3 metadata using eyed3 lib
'''
from os.path import isfile
from typing import List
import getopt, sys, os

arg_list = sys.argv[1:]

# command line arguments
options = "m:a:"
# long options
long_options = ["music=", "art="]
value_map = {}


def parse_eyed3_options() -> dict:
    try:
        arguments, _ = getopt.getopt(arg_list, options, long_options)
        # check each argument present
        for curr_arg, curr_value in arguments:
            if curr_arg in ("-m", "--music"):
                if os.path.isfile(curr_value) and curr_value.endswith('mp3'):
                    value_map['music'] = curr_value
                else:
                    print('Wrong music path entered, try again!')
                # print(f"Music path is {curr_value}")
            if curr_arg in ("-a", "--art"):
                if os.path.isfile(curr_value) and (curr_value.endswith('jpg') or curr_value.endswith('png') or curr_value.endswith('jpeg')):
                    value_map['art'] = curr_value
                else:
                    print('Wrong artfile path entered')
                # print(f"Art path is {curr_value}")
        # print(f"Value list is: {str(value_map)}")
    except getopt.error as err:
        print (str(err))

    return value_map

# FOR TESTING
if __name__ == "__main__":
    parse_options()

