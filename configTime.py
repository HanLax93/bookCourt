import time
import datetime as dt
import ntplib
import numpy as np

from main import getParser
from processData import cryptCBCPkcs7


class configureTime:
    def __init__(self):  # init the delay with 0 and the timing time
        self.delay = 0
        self.timingTime = self.setTime()

    def countTo2(self):  # countdown to last 2 min
        self.getTimeDelay()
        flag = True
        while flag:
            if self.getLocalInterval() > 120:
                time.sleep(60)
            else:
                flag = False
        self.getTimeDelay()

    def getTimeDelay(self):  # get delay between local time and server time
        timeDelay = np.zeros([10])  # take the average of ten items as delay
        for i in range(10):
            ntpClient = ntplib.NTPClient()
            times = ntpClient.request("edu.ntp.org.cn", version=2)  # get the server time from the china education web
            timeDelay[i] = times.tx_time + times.delay / 2 - time.time()
        self.delay = np.average(np.array(timeDelay))

    def getInterval(self):  # get time interval between server time and timing time
        ntpClient = ntplib.NTPClient()
        interval = self.timingTime - ntpClient.request("edu.ntp.org.cn", version=2, timeout=3).tx_time
        return interval

    def getLocalInterval(self):  # get the time interval between local time and timing time but within delay
        localTimestamp = time.time()
        interval = self.timingTime - localTimestamp - self.delay
        return interval

    @staticmethod
    def getTimeVerify():  # get signature value of timestamp when request sends
        key = "6f00cd9cade84e52"
        iv = "25d82196341548ef"
        cryptor = cryptCBCPkcs7(key, iv)
        TS = str(round(time.time() * 1000))
        TSS = cryptor.encrypt(TS).decode()
        return TS, TSS

    @staticmethod
    def getNtpTime():  # just get the server time
        ntpClient = ntplib.NTPClient()
        times = ntpClient.request("edu.ntp.org.cn", version=2).tx_time
        localTime = time.localtime(ntpClient.request("edu.ntp.org.cn", version=2).tx_time)
        localTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        return times, localTime + str(times % 1)

    @staticmethod
    def setTime():  # get the timestamp of timing time
        th, tm, ts, _ = getParser()
        today = "{:%Y-%m-%d}".format(dt.datetime.now())
        tm = tm + 1 if ts == 59 else tm
        th = th + 1 if tm == 60 else th
        ts = ts + 1
        ts = 0 if ts == 60 else ts
        tm = 0 if tm == 60 else tm
        ret_hour = str(th)
        ret_min = '0' + str(tm) if tm <= 9 else str(tm)
        ret_sec = '0' + str(ts) if ts <= 9 else str(ts)
        ret = today + ' ' + ret_hour + ':' + ret_min + ':' + ret_sec
        ret = time.strptime(ret, '%Y-%m-%d %H:%M:%S')
        return time.mktime(ret)
