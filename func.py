import json
import time
import requests
import datetime as dt

from basicConfig import *
from configTime import configureTime
from processData import get_key
from main import getParser


class func:
    def __init__(self, myToken):  # init with host and token
        self.host = host
        self.token = myToken

    def cancelCourt(self):  # you can try to cancel the booking with this function
        data = self.getPriLogs()
        stadiumId = data['data'][0]['id']  # the id of the latest court booking
        params = {"logId": str(stadiumId)}  # request params
        params = json.dumps(params)

        url = self.host + "/user/cancel"  # url to which cancel request post
        headers = basicHeaders
        headers.update({"Token": self.token, "Content-Type": "application/x-www-form-urlencoded"})  # request headers
        s = requests.post(url, params, headers=headers)  # response information
        return s.json

    def bookBadminton(self, p):  # try to book a Badminton court
        today = '{:%Y-%m-%d}'.format(dt.datetime.now())  # the date today
        params = {
            "periodId": p[0],
            "date": today,
            "stadiumId": p[1]
        }  # request params including the id and the time you want to book
        params = json.dumps(params)
        url = self.host + "/user/book"  # url to which book request post
        timestamp, timestampSignature = configureTime().getTimeVerify()  # time and signature time when request sends
        headers = basicHeaders
        headers.update({"token": self.token, "Resultjson": timestamp, "Content-Type": "application/json",
                        "Resultjsonsignature": timestampSignature, "Content-Length": "49"})  # request headers
        # print("数据提交时间：", dt.datetime.now())  # print the time when the request sends
        s = requests.post(url, params, headers=headers)  # response information including the result of booking
        return s.json()

    def getPriLogs(self):  # get the latest booking info
        # limit param means only return the latest booking info
        params = {"containCanceled": "false", "desc": "true", "limit": "1", "offset": "0"}
        params = json.dumps(params)
        url = self.host + "/user/getPriLogs"  # url to which query request post
        headers = basicHeaders
        # request headers
        headers.update({"token": self.token, "Content-Length": "59", "Content-Type": "application/json"})
        s = requests.post(url, params, headers=headers).json()
        # resolve the serial number of the court from the response info
        court = get_key(stadiumIdList, str(s["data"][0]["stadiumId"]))[0]
        infoSum = "The latest:\n" + court + '\n' + s['data'][0]['period'] + '\n' + s['data'][0]['date']
        print(infoSum)
        return s

    def bookCourt(self, params):  # countdown and book
        _, _, _, t_delay = getParser()  # get delay microseconds
        t = configureTime()
        t.countTo2()  # countdown to last 2 min
        flag = True
        # countdown to the timing time
        while flag:
            time.sleep(0.989)
            # print(getLocalInterval(rt, de))
            if t.getLocalInterval() <= 2:
                while flag:
                    # time.sleep(0.003)
                    # print(getLocalInterval(ringTime, de))
                    if t.getLocalInterval() <= t_delay:
                        info = self.bookBadminton(params)
                        print("数据返回时间：", dt.datetime.now())
                        print(info)
                        flag = False
        # print the latest booked court after 5 sec
        time.sleep(5)
        self.getPriLogs()
