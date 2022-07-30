from urllib import request
import json
import xlwt
import datetime
import operationPath
import sendFile
import combineExcle
import time
import setBorder
import handleFile
import sendFile_special


# 获取接口内容
def get_html():
    url = "https://bshop.guanmai.cn/product/sku/get?level=1&category_id="
    # A118200 野菜  A6988 时令蔬菜  A6982 肉禽类   A6986 水果类
    key = ["A6988","A6982","A6986"]
    headers = {
        "Cookie": "cms_key=srfc; group_id=630; gr_user_id=7b087989-dc51-4066-94f6-bf064a0b05d2; 9beedda875b5420f_gr_session_id=0168e4b9-f768-4690-ba26-5564f1ee94e9; 9beedda875b5420f_gr_session_id_0168e4b9-f768-4690-ba26-5564f1ee94e9=true; Hm_lvt_d02cd7e3028015e0088f63c017c81147=1654602700; sessionid=rrdk63iop731j3ruvq8fadcp0ga3qf61; Hm_lpvt_d02cd7e3028015e0088f63c017c81147=1654602754; 9beedda875b5420f_gr_last_sent_sid_with_cs1=0168e4b9-f768-4690-ba26-5564f1ee94e9; 9beedda875b5420f_gr_last_sent_cs1=1801126; 9beedda875b5420f_gr_cs1=1801126"
    }
    html = []
    for i,j in enumerate(key):
        newUrl = url + j;
        req = request.Request(url=newUrl, headers=headers)
        res = request.urlopen(req)
        html.append(res.read().decode("utf-8", "ignore"))

    # windows会存在乱码问题，需要使用 gbk解码，并使用ignore忽略不能处理的字节
    # linux不会存在上述问题，可以直接使用decode('utf-8')解码
    return html

def getStyle(stype):

    # 表头
    if stype == "title":
        # 字体格式
        style = xlwt.XFStyle()
        titlefont = xlwt.Font()
        titlefont.name = "宋体"
        titlefont.height = 16 * 20
        style.font = titlefont
        # 表头单元格格式
        align = xlwt.Alignment()
        align.horz = 0x02
        align.vert = 0x01
        style.alignment = align
        return style

        # 表头
    if stype == "title1":
        # 字体格式
        style = xlwt.XFStyle()
        titlefont = xlwt.Font()
        titlefont.name = "宋体"
        titlefont.height = 14 * 20
        style.font = titlefont
        # 表头单元格格式
        align = xlwt.Alignment()
        align.horz = 0x02
        align.vert = 0x01
        style.alignment = align
        return style
    #单元格格式
    if stype == "cell":
        style = xlwt.XFStyle()
        titlefont = xlwt.Font()
        titlefont.name = "宋体"
        titlefont.height = 11 * 20
        style.font = titlefont
        # 表头单元格格式
        align = xlwt.Alignment()
        align.vert = 0x01
        style.alignment = align
        return style


# 解析json并将内容输出到邮件
def saveExcleOnDay(html):
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    weekday = datetime.datetime.now().weekday()

    workbook = xlwt.Workbook()  # 打开一个工作簿
    # 创建一个worksheet
    worksheet = workbook.add_sheet(now + "(" + handleFile.getWeekDayName(weekday) + ")")
    for i in range(0,3):
        first_col = worksheet.col(i*3)  # 获取第一列
        first_col.width = 256 * 20  # 设置第一列列宽
    tall_style = xlwt.easyxf('font:height 400')  # 设置行高
    worksheet.write_merge(0, 0, 0, 8, "幼鲜知价格表（" + now + "）            单位：元/斤",getStyle("title"))
    worksheet.write_merge(1, 1, 0, 2, "幼鲜知蔬菜价格表",getStyle("title1"))
    worksheet.write_merge(1, 1, 3, 5, "幼鲜知肉禽价格表",getStyle("title1"))
    worksheet.write_merge(1, 1, 6, 8, "幼鲜知水果价格表",getStyle("title1"))
    for i in range(0,2):
        row = worksheet.row(i)
        row.set_style(tall_style)  # 设置行高
    for i,data in enumerate(html):
        worksheet.write(2,i*3+0,"品名",getStyle("title1"))
        worksheet.write(2,i*3+1,"价格",getStyle("title1"))
        worksheet.write(2,i*3+2,"单位",getStyle("title1"))
        for j, row in enumerate(json.loads(data).get("data")):
            worksheet.write(j+3,i*3+0,row.get("name"),getStyle("cell"))
            worksheet.write(j+3,i*3+1,row.get("std_sale_price")/100,getStyle("cell"))
            worksheet.write(j+3,i*3+2,row.get("std_unit_name"),getStyle("cell"))
            first_row = worksheet.row(j + 3)
            first_row.set_style(tall_style)  # 设置行高
    workbook.save(now+"("+ handleFile.getWeekDayName(weekday)+ ")" + ".xls")

def main():
    try:
        print("小助手运行中......")
        while True:
            # now = datetime.datetime.now().strftime('%Y-%m-%d')
            now = datetime.datetime.now().weekday()
            # 确保只发送周五往前推一个周的数据
            if now != 4 :
                now = ((datetime.datetime.now())+datetime.timedelta(days= 4-now)).strftime('%Y-%m-%d')
            weekday = 4
            nowTime = time.strftime("%H:%M:%S")
            if time.strptime(nowTime, "%H:%M:%S").__ge__(time.strptime("08:30:00", "%H:%M:%S")) and operationPath.containFile(datetime.datetime.now().strftime('%Y-%m-%d')+"("+ handleFile.getWeekDayName(datetime.datetime.now().weekday())+ ")"+ ".xls"):
                # 保存当天的excle
                saveExcleOnDay(get_html())
                print("保存当天文件成功: " + now)
            if operationPath.containFile(str(now) + "(" + handleFile.getWeekDayName(weekday) + ")" + "--") and operationPath.containFile(datetime.datetime.now().strftime('%Y-%m-%d') + "(" + handleFile.getWeekDayName(
                                    datetime.datetime.now().weekday()) + ")" + "--"):
                if (time.strptime(nowTime, "%H:%M:%S").__ge__(
                            time.strptime("08:30:00", "%H:%M:%S")) and datetime.datetime.now().weekday() >= 4):
                        # pass
                    # 合并当周获取的文件
                    print("合并当周获取的文件")
                    title = combineExcle.combineExcle()
                    # 设置边框样式
                    sheets = handleFile.getDatePath(False)
                    setBorder.getFileAndSetStype(title, sheets)
                    # 发送至指定邮箱到公共区域
                    msg = title + "幼鲜知价格表"
                    print("发送至指定邮箱 到 公共区域")
                    message = sendFile.message_config(msg)
                    sendFile.send_mail(message)
                    print("发给小主子.....")
                    msg = msg + "准备好啦"
                    message = sendFile_special.message_config(msg)
                    sendFile_special.send_mail(message)
                    print("当周数据完成!!!     " + title)
                    print("准备删除上周文件....")
                    operationPath.removeWeekFile()
                    print("删除成功...")
    except Exception as e:
        print("获取失败!!!!!!")
        print(e)

if __name__ == '__main__':
    main()