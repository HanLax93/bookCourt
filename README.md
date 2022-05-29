# bookCourt
## Wechat packet capture:

1.Setup [`Proxifier`](https://www.proxifier.com/)
  
  - Profiles - Proxy Servers -Add:
    
    - Address: 127.0.0.1
      
    - Port: $PORT
      
    - Protocol: HTTPS
      
  - Proxification Rules - Add:
    
    - Name: $CUSTOM
      
    - Applications: every *WeChatApp.exe*、every *WeChatAppEx.exe*
      
    - Action: Proxy HTTPS 127.0.0.1
      
  - Enable $CUSTOM and set *Localhost* as Direct
  
2.Setup [`Burp Suite`](https://portswigger.net/burp)
  
  - Proxy - Options -Proxy Listenners:
    
    - Bind to port: $PORT
      
    - Bind to adderss: *Loopback only*
    
3.Open mini program

4.Burp Suite - Proxy - Intercept - Intercept is on

## How to use:
1.Fill your own token in *./config/config.yaml*:
````yaml
tokens:
  myToken: 13673187-6798-435e-8e32-06fb6cac3a50
````
- Notice: the token expired <u>every 24 hours</u>.

2.Change your booking info in *main.py*:
````python
courtTime, court = config['periodIdList']["Badminton 16to17"], config['stadiumIdList']["Badminton court4"]
myBookInfo = [courtTime, court]
````
- Notice: you can find other keys in variable *stadiumIdList* and *periodIdList*

3.Change values *token* and bookInfo in *main.py* to two above values:

````python

from application import modules

myToken = config['tokens']['myToken']

f = func.Features(myToken, config)  # put your token here
f.getPriLogs()
f.bookCourt(myBookInfo)  # put your book info here
````

## Tips:
path of *WeChatApp.exe*:
````shell
C:\Users\$USERNAME\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\XWeb\$RANDOM_NUMBER\extracted\wechatapp.exe
````
- Note: find all WeChatApp.exe in every `$RANDOM_NUMBER` folder.

path of *WeChatAppEx.exe*:
````shell
C:\Users\$USERNAME\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\WMPFRuntime\$RANDOM_NUMBER\extracted\runtime\WeChatAppEx.exe
````
- Note: find all WeChatAppEx.exe in every `$RANDOM_NUMBER` folder.

token is here:
![](./src/img.png)