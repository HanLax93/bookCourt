# Please adjust the delay according to the computer time this script running on referring to the website time.is
# The post time should be about 11:59:59:300

import json
import math
import time
import datetime as dt
import requests
import base64
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms

stadiumIdList = {
    "Badminton court1": "5",
    "Badminton court2": "6",
    "Badminton court3": "7",
    "Badminton court4": "8",
    "Badminton court5": "13",
    "Badminton court6": "14",
    "Tennis court1": "9",
    "Tennis court2": "10",
    "Tennis court3": "11",
    "Tennis court4": "12"
}

periodIdList = {
    "Badminton 15to16": "22",
    "Badminton 16to17": "2",
    "Badminton 17to18": "3",
    "Badminton 18to19": "4",
    "Badminton 19to20": "5",
    "Badminton 20to21": "6",
    "Tennis 19to20": "27",
    "Tennis 20to21": "28",
}

basicHeaders = {
    "Host": "tyb.qingyou.ren",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/4347 "
                  "MicroMessenger/8.0.22.2140(0x280016F7) WeChat/arm32 Weixin NetType/WIFI Language/zh_CN "
                  "ABI/arm32 "
                  "MiniProgramEnv/android",
    "Charset": "utf-8",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://servicewechat.com/wxebade4c4672d5e61/13/page-frame.html"
}


def pkcs7_padding(data):
    if not isinstance(data, bytes):
        data = data.encode()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    return padded_data


class cryptCBCPkcs7(object):

    def __init__(self, key: str, iv: str):
        self.ciphertext = " "
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
        self.iv = iv.encode('utf-8')

    def encrypt(self, text: str):
        cryptor = AES.new(self.key, self.mode, self.iv)

        text = text.encode('utf-8')
        text = pkcs7_padding(text)
        self.ciphertext = cryptor.encrypt(text)

        return base64.b64encode(self.ciphertext)


def getTimeVerify():
    key = "6f00cd9cade84e52"
    iv = "25d82196341548ef"
    cryptor = cryptCBCPkcs7(key, iv)
    TS = str(round(time.time() * 1000))
    TSS = cryptor.encrypt(TS).decode()
    return TS, TSS


def bookBadminton(mhost, mtoken):
    today = '{:%Y-%m-%d}'.format(dt.datetime.now())
    params = {
        "periodId": periodIdList["Badminton 16to17"],
        "date": today,
        "stadiumId": stadiumIdList["Badminton court4"]
    }
    url = mhost + "/user/book"
    params = json.dumps(params)
    timestamp, timestampSignature = getTimeVerify()
    headers = basicHeaders
    headers.update({"token": mtoken, "Resultjson": timestamp, "Content-Type": "application/json",
                                   "Resultjsonsignature": timestampSignature, "Content-Length": "49"})
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


def get_key(d, value):
    k = [k for k, v in d.items() if v == value]
    return k


def Countdown(flag, m, s, mtoken):
    while flag:
        time.sleep(1)
        if (dt.datetime.now().second >= (s - 1)) & (dt.datetime.now().minute == m):
            while flag:
                time.sleep(0.02)
                if dt.datetime.now().second >= s:
                    while flag:
                        time.sleep(0.01)
                        if (math.fabs(dt.datetime.now().microsecond - 450000)) <= 20000:
                            info = bookBadminton(host, mtoken)
                            print(info)
                            # print("now: ", dt.datetime.now())
                            flag = False


if __name__ == '__main__':
    minute = 35
    second = 59
    host = "https://tyb.qingyou.ren"
    token_han = "a80340b7-355f-4dd5-b396-75e30045ed67"
    token_lzw = "9b32a80f-6c0f-451c-80d4-7cbaeb48862d"
    notTwelve = True
    getPriLogs(host, token_lzw)
    Countdown(notTwelve, minute, second, token_lzw)
    time.sleep(5)
    getPriLogs(host, token_lzw)
