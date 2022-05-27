# Please adjust the delay according to the computer time this script running on referring to the website time.is
# The post time should be about 12:00:00:300

import argparse
from func import *


def getParser():  # provide a entrance for custom timing time test
    myParser = argparse.ArgumentParser(description='timeSetting')
    myParser.add_argument('-hr', '--hour', type=int, default=12, help='setup hour part')
    myParser.add_argument('-m', '--min', type=int, default=0, help='setup minute part')
    myParser.add_argument('-s', '--sec', type=int, default=0, help='setup second part')
    myParser.add_argument('-d', '--delay', type=int, default=300, help='setup microsecond part')
    a = myParser.parse_args()
    t_h = a.hour
    t_m = a.min
    t_s = a.sec
    t_d = 1 - a.delay/1000
    return t_h, t_m, t_s, t_d


if __name__ == '__main__':
    f = func(token_han)  # put your token here
    f.getPriLogs()
    f.bookCourt(bookInfo)  # put your book info here
