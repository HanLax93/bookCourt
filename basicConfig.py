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
    "Badminton 15.5to16": "21",
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

bookInfo = [periodIdList["Badminton 16to17"], stadiumIdList["Badminton court4"]]
host = "https://tyb.qingyou.ren"
token_han = "65bf8159-4232-44ec-9d39-8af04c4ba0d4"  # 22-05-24 11:30 needs to be updated every day.
token_lzw = "13673187-6798-435e-8e32-06fb6cac3a50"  # aborted
token_mys = ""
