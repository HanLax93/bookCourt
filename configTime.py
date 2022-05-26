import time
import datetime as dt
import ntplib
import numpy as np

from processData import cryptCBCPkcs7


def getTimeDelay():
    timeDelay = np.zeros([10])
    for i in range(10):
        ntpClient = ntplib.NTPClient()
        times = ntpClient.request("edu.ntp.org.cn", version=2)
        timeDelay[i] = times.tx_time + times.delay / 2 - time.time()
    timeDelay = np.average(np.array(timeDelay))
    return timeDelay


def getInterval(rt):
    ntpClient = ntplib.NTPClient()
    interval = rt - ntpClient.request("edu.ntp.org.cn", version=2, timeout=3).tx_time
    return interval


def getNtpTime():
    ntpClient = ntplib.NTPClient()
    times = ntpClient.request("edu.ntp.org.cn", version=2).tx_time
    localTime = time.localtime(ntpClient.request("edu.ntp.org.cn", version=2).tx_time)
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    return times, localTime + str(times % 1)


def getLocalInterval(rt, de):
    localTimestamp = time.time()
    interval = rt - localTimestamp - de
    return interval


def getTimeVerify():
    key = "6f00cd9cade84e52"
    iv = "25d82196341548ef"
    cryptor = cryptCBCPkcs7(key, iv)
    TS = str(round(time.time() * 1000))
    TSS = cryptor.encrypt(TS).decode()
    return TS, TSS


def setTime(th, tm, ts):
    today = "{:%Y-%m-%d}".format(dt.datetime.now())
    ret0 = today + ' ' + str(th) + ':'
    ret1 = ret0 + '0' + str(tm) + ':' if ts <= 9 else ret0 + str(tm) + ':'
    ret = ret1 + '0' + str(ts+1) if ts <= 8 else ret1 + str(ts+1)
    ret = time.strptime(ret, '%Y-%m-%d %H:%M:%S')
    ret = time.mktime(ret)
    return ret


def countTo2(rt):
    de = getTimeDelay()
    flag = True
    while flag:
        if getLocalInterval(rt, de) > 120:
            time.sleep(60)
        else:
            de = getTimeDelay()
            flag = False
    return de


