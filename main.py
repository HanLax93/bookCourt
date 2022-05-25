# Please adjust the delay according to the computer time this script running on referring to the website time.is
# The post time should be about 11:59:59:500

import json
import time
import requests
import datetime as dt
import argparse
from basicConfig import basicHeaders, stadiumIdList, host, token_han, bookInfo
from configTime import getLocalInterval, getTimeVerify, getTimeDelay, setTime, countTo2
from processData import get_key


def getParser():
    myParser = argparse.ArgumentParser(description='timeSetting')
    myParser.add_argument('--hour', type=int, default=12, help='setup hour part')
    myParser.add_argument('--min', type=int, default=1, help='setup minute part')
    myParser.add_argument('--sec', type=int, default=0, help='setup second part')
    myParser.add_argument('--tms', type=int, default=300, help='setup microsecond part')
    a = myParser.parse_args()
    t_h = a.hour
    t_m = a.min
    t_s = a.sec
    t_mm = a.tms
    return t_h, t_m, t_s, t_mm


def bookBadminton(mhost, mtoken, p):
    today = '{:%Y-%m-%d}'.format(dt.datetime.now())
    params = {
        "periodId": p[0],
        "date": today,
        "stadiumId": p[1]
    }
    params = json.dumps(params)
    url = mhost + "/user/book"
    timestamp, timestampSignature = getTimeVerify()
    headers = basicHeaders
    headers.update({"token": mtoken, "Resultjson": timestamp, "Content-Type": "application/json",
                    "Resultjsonsignature": timestampSignature, "Content-Length": "49"})
    print("数据提交时间：", dt.datetime.now())
    s = requests.post(url, params, headers=headers)
    return s.json()


def getPriLogs(mhost, mtoken):
    params = {"containCanceled": "false", "desc": "true", "limit": "1", "offset": "0"}
    params = json.dumps(params)
    url = mhost + "/user/getPriLogs"
    headers = basicHeaders
    headers.update({"token": mtoken, "Content-Length": "59", "Content-Type": "application/json"})
    s = requests.post(url, params, headers=headers).json()
    court = get_key(stadiumIdList, str(s["data"][0]["stadiumId"]))[0]
    infoSum = "The latest:\n" + court + '\n' + s['data'][0]['period'] + '\n' + s['data'][0]['date']
    print(infoSum)


def countDown(rt, de, tms, mhost, mtoken, params):
    flag = True
    while flag:
        time.sleep(0.989)
        # print(getLocalInterval(rt, de))
        if getLocalInterval(rt, de) <= 2:
            while flag:
                # time.sleep(0.003)
                # print(getLocalInterval(rt, de))
                if getLocalInterval(rt, de) <= tms:
                    info = bookBadminton(mhost, mtoken, params)
                    print("数据返回时间：", dt.datetime.now())
                    print(info)
                    flag = False


if __name__ == '__main__':
    t_hour, t_min, t_sec, t_ms = getParser()

    ringTime = setTime(t_hour, t_min, t_sec)
    delay = countTo2(ringTime)

    getPriLogs(host, token_han)
    countDown(ringTime, delay, 1-t_ms/1000, host, token_han, bookInfo)
    time.sleep(5)
    getPriLogs(host, token_han)
