# Please adjust the delay according to the computer time this script running on referring to the website time.is
# The post time should be about 12:00:00:300
import argparse
from application import modules
import yaml


def getPars():  # provide a entrance for custom timing time test
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
    t = [t_h, t_m, t_s, t_d]
    return t


def getConfig():
    file = open("./config/config.yaml", 'r', encoding="utf-8")
    data = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return data


class app:
    def __init__(self, config):
        self.config = config

    def main(self):
        delayms = int(self.config['delayms'])
        t = [12, 0, 0, 1-delayms/1000]
        self.config.update({'time': t})

        token = self.config['topToken']
        courtTime, court = self.config['topCourtTime'], self.config['topCourt']
        bookInfo = [courtTime, court]

        f = modules.Features(token, self.config)  # put your token here
        _, ver = f.getPriLogs()
        print(ver)
        info, info2 = f.bookCourt(bookInfo)  # put your book info here

        return info, info2
