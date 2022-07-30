from urllib import request
import json
import xlwt
import datetime
import time
import sendFile
import sendHeartbeart


# 获取接口内容
def get_html(url, headers):
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    # windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
    # linux不会存在上述问题，可以直接使用decode('utf-8')解码
    html = res.read().decode("utf-8", "ignore")
    return html


# 解析json并将内容输出到邮件
def parseJson(string,var):
    obj = json.loads(string)
    print(obj["data"])
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet' + var)
    worksheet.write(0, 0, label="商品名称")
    worksheet.write(0, 1, label="商品价格")
    b=0
    for i in obj["data"]:
        b= b+1
        # print(b)
        # 写入excel
        # 参数对应 行, 列, 值
        worksheet.write(b, 0, label=i["name"])
        worksheet.write(b, 1, label=str(i["std_sale_price"]/100) + "/" + i["std_unit_name"])
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    if obj["data"] != None and len(obj["data"]) > 1:
        print("以获取到: " + now + " 数据")
    if var=="A118200":
        workbook.save(now + "--" + "野菜" + '.xls')
    elif var=="A6988":
        workbook.save(now + "--" + "时令蔬菜" + '.xls')
    elif var=="A6982":
        workbook.save(now + "--" + "肉禽类" + '.xls')
    elif var=="A6986":
        workbook.save(now + "--" + "水果类" + '.xls')
if __name__=='__main__':
    # url = "https://bshop.guanmai.cn/product/sku/get?level=1&category_id=A6988"
    url = "https://bshop.guanmai.cn/product/sku/get?level=1&category_id="
    # A118200 野菜  A6988 时令蔬菜  A6982 肉禽类   A6986 水果类
    key = ["A6988","A118200","A6982","A6986"]
    headers = {
        # "X-Guanmai-Client": "GmBshop/4.0.0 3d85cc9ffbbbdf42e1b14fc0334857b2",
        "Cookie": "cms_key=srfc; group_id=630; gr_user_id=7b087989-dc51-4066-94f6-bf064a0b05d2; 9beedda875b5420f_gr_session_id=0168e4b9-f768-4690-ba26-5564f1ee94e9; 9beedda875b5420f_gr_session_id_0168e4b9-f768-4690-ba26-5564f1ee94e9=true; Hm_lvt_d02cd7e3028015e0088f63c017c81147=1654602700; sessionid=rrdk63iop731j3ruvq8fadcp0ga3qf61; Hm_lpvt_d02cd7e3028015e0088f63c017c81147=1654602754; 9beedda875b5420f_gr_last_sent_sid_with_cs1=0168e4b9-f768-4690-ba26-5564f1ee94e9; 9beedda875b5420f_gr_last_sent_cs1=1801126; 9beedda875b5420f_gr_cs1=1801126",
        # # "X-Guanmai-Request-Id": "53a0797d-745a-42fa-83d6-d75decd58849",
        # "X-Guanmai-Success-Code": 0,
        # "X-Guanmai-Timeout": 30000
    }
    # schedule.every().day.at("8:30").do(parseJson(get_html(url,headers)))  # 每天八点半执行
    print("程序开始执行......")
    while True:
        now = time.strftime("%H:%M:%S")
        if (now.__contains__("12")):
            sendHeartbeart.getBaidu()
            time.sleep(60)
        if (now == "08:30"):
            for i in key:
                newUrl = url + i;
                print(now)
                parseJson(get_html(newUrl, headers), i)
            print("今日数据获取完毕!!!")
            print("准备发送邮件......")
            message = sendFile.message_config()
            sendFile.send_mail(message)
            time.sleep(60)
    # for i in key:
    #     newUrl = url + i;
    #     parseJson(get_html(newUrl, headers), i)
    # print("今日数据获取完毕!!!")
    # print("准备发送邮件......")
    # message = sendFile.message_config()
    # sendFile.send_mail(message)
    # time.sleep(60)

