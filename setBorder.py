import xlwings as xw
import os
import pythoncom

#打开存好的excel
file_list = os.listdir(os.getcwd())


def getFileAndSetStype(file,sheets):
    pythoncom.CoInitialize()
    app = xw.App()  # 设置应用
    wb = xw.Book(file)  # 打开文件
    for i in sheets:
        try:
            ws = wb.sheets[i]  # 选择表格
            setBorderStyle(ws)
        except:
            print("没有该表名!!!!!")
            pass
    # 保存并关闭excel
    wb.save(file)
    wb.close()
    app.quit()

def setBorderStyle(ws):
    last_row3 = ws.range('G2:I2').end('down').row  # 水果类
    setSubBorder(ws,'G','I',last_row3)
    last_row2 = ws.range('D2:F2').end('down').row  # 肉禽
    setSubBorder(ws, 'D', 'F', last_row2)
    last_row1 = ws.range('A2:C2').end('down').row  # 蔬菜
    setSubBorder(ws, 'A', 'C', last_row1)
    a_range = f'A1:I2'  # 生成表格的数据范围
    setborder(ws,a_range)

#设置边框
def setborder(ws,range):
    ws.range(range).api.Borders(8).LineStyle = 1  # 上边框
    ws.range(range).api.Borders(9).LineStyle = 1  # 下边框
    ws.range(range).api.Borders(7).LineStyle = 1  # 左边框
    ws.range(range).api.Borders(10).LineStyle = 1  # 右边框
    ws.range(range).api.Borders(12).LineStyle = 1  # 内横边框
    ws.range(range).api.Borders(11).LineStyle = 1  # 内纵边框


def setSubBorder(ws,rwo1, row2,last_row):
    ws.range(f'{rwo1}2:{row2}{last_row}').api.Borders(8).LineStyle = 1  # 上边框
    ws.range(f'{rwo1}2:{row2}{last_row}').api.Borders(9).LineStyle = 1  # 下边框
    ws.range(f'{rwo1}2:{row2}{last_row}').api.Borders(7).LineStyle = 1  # 左边框
    ws.range(f'{rwo1}2:{row2}{last_row}').api.Borders(10).LineStyle = 1  # 右边框


if __name__=="__main__":
    getFileAndSetStype("2022-07-19(周二)--2022-07-13(周三).xls",["2022-06-20(周一)","2022-06-21(周二)"])