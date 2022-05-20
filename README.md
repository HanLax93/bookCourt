# bookCourt
## 微信小程序抓包：

1. 打开全局代理（windows端使用 [`Proxifier`](https://www.proxifier.com/)）
  
  - Profiles - Proxy Servers -Add:
    
    - Address: *$address*
      
    - Port: *$port*
      
    - Protocol: HTTPS
      
  - Proxification Rules - Add:
    
    - Name: *$custom*
      
    - Applications: every *wechatapp.exe*、*wechatappex.exe*
      
    - Action: Proxy HTTPS 127.0.0.1
      
  - 启用 *$custom* 并将 *Localhost* 设为 Direct
    
2. 设置 [`Burp Suite`]([https://www.proxifier.com/](https://portswigger.net/burp)
  
  - Proxy - Options -Proxy Listenners:
    
    - Bind to port: *$port*
      
    - Bind to adderss: *Loopback only*
      
3. Burp Suite - Proxy - Intercept - Intercept is on: 开始抓包
