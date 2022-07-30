import requests
import time

def getBaidu():
    url = "http://www.baidu.com"
    content = requests.get(url)
    print(content)
    if content.status_code == 200:
        print("发送心跳成功.....")
def beSend():
    flag = True
    now = time.strftime("%R")
    if (now.__contains__("02") and flag):
        getBaidu()
if __name__ == '__main__':
    getBaidu()