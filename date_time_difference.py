from ctypes import string_at
import datetime
import logging
# custom
from util.parse_time_diff_args import parse_time_args

"""
DateTime Difference calculator
example: python .\date_time_difference.py -s '23/04/12 15:10:00' -e '23/04/12 15:45:00'
"""
def main():
    time_obj: dict = parse_time_args()
    logging.debug("start and end time is {}".format(str(time_obj)))
    try:
        start_time = time_obj.get('start', None)
        end_time = time_obj.get('end', None)
        if start_time is None or end_time is None: 
            raise ValueError("Please provide valid start and end datetime")
        dt1 = datetime.datetime.strptime(start_time, "%y/%m/%d %H:%M:%S") 
        dt2 = datetime.datetime.strptime(end_time, "%y/%m/%d %H:%M:%S") 
        tdelta = dt2 - dt1
        print("Time difference is {}".format(tdelta))
    except Exception as err:
        print("Invalid format {}".format(str(err)))

if __name__ == "__main__":
    main()
