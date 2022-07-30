from urllib import request
import requests
import time

def getAPI(phone):
    url = "http://www.jutixueyuan.com/user/api/user/send/code"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
        "Host": "www.jutixueyuan.com",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "http://www.jutixueyuan.com/login",
        "Origin": "http://www.jutixueyuan.com",
        "orgno": "yunti",
        "token": "null",
        "Content-Length": "72",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache"
    }
    data = {"clientId": "lkb65617f842ad4c37895a733b8de43cbb", "mobile": phone}
    req = requests.post(url=url, json=data, headers=headers)
    print(req.status_code)
    return req.status_code

if __name__ == "__main__":
    while True:
        code = getAPI("18168481525")
        print("发送成功")
        time.sleep(60)