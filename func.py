import json
import time
import requests
import datetime as dt

from basicConfig import *
from configTime import configureTime
from processData import get_key
from main import getParser


class func:
    def __init__(self, myHost, myToken):
        self.host = myHost
        self.token = myToken

    def cancelCourt(self):
        data = self.getPriLogs()
        stadiumId = data['data'][0]['id']
        params = {"logId": str(stadiumId)}
        params = json.dumps(params)

        url = self.host + "/user/cancel"
        headers = basicHeaders
        headers.update({"Token": self.token, "Content-Type": "application/x-www-form-urlencoded"})
        s = requests.post(url, params, headers=headers)
        return s.json

    def bookBadminton(self, p):
        today = '{:%Y-%m-%d}'.format(dt.datetime.now())
        params = {
            "periodId": p[0],
            "date": today,
            "stadiumId": p[1]
        }
        params = json.dumps(params)
        url = self.host + "/user/book"
        timestamp, timestampSignature = configureTime().getTimeVerify()
        headers = basicHeaders
        headers.update({"token": self.token, "Resultjson": timestamp, "Content-Type": "application/json",
                        "Resultjsonsignature": timestampSignature, "Content-Length": "49"})
        print("数据提交时间：", dt.datetime.now())
        s = requests.post(url, params, headers=headers)
        return s.json()

    def getPriLogs(self):
        params = {"containCanceled": "false", "desc": "true", "limit": "1", "offset": "0"}
        params = json.dumps(params)
        url = self.host + "/user/getPriLogs"
        headers = basicHeaders
        headers.update({"token": self.token, "Content-Length": "59", "Content-Type": "application/json"})
        s = requests.post(url, params, headers=headers).json()
        court = get_key(stadiumIdList, str(s["data"][0]["stadiumId"]))[0]
        infoSum = "The latest:\n" + court + '\n' + s['data'][0]['period'] + '\n' + s['data'][0]['date']
        print(infoSum)
        return s

    def bookCourt(self, params):
        _, _, _, t_delay = getParser()
        t = configureTime()
        t.countTo2()
        flag = True
        while flag:
            time.sleep(0.989)
            # print(getLocalInterval(rt, de))
            if t.getLocalInterval() <= 2:
                while flag:
                    # time.sleep(0.003)
                    # print(getLocalInterval(ringTime, de))
                    if t.getLocalInterval() <= t_delay:
                        # info = self.bookBadminton(params)
                        print("数据返回时间：", dt.datetime.now())
                        # print(info)
                        flag = False
        time.sleep(5)
        self.getPriLogs()
