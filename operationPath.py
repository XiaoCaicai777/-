# 导入os模块
import os
import datetime
import handleFile
import sys
# os.listdir()方法获取文件夹名字，返回数组
def getPath():
    try:
        file_name_list = os.listdir(os.getcwd())
        excles = []
        for file in file_name_list:
            if file.__contains__(".xls"):
                excles.append(file)
        # print("获取当前工作路径的excle成功......")
        return excles
    except Exception as e:
        print(e)
        print("获取当前工作路径下的excle文件失败!!!!")

def getEmailConfigFile():
    try:
        file_name_list = os.listdir(os.getcwd())
        for file in file_name_list:
            if file.__contains__("email_config.dls"):
                return True
        # print("获取当前工作路径的excle成功......")
        return False
    except Exception as e:
        print(e)
        print("获取当前工作路径下的email_config.txt文件失败!!!!")

def removeWeekFile():
    excles = getPath()
    for num,file in enumerate(excles):
        if len(excles) > 8:
            if num < 8:
                try:
                    os.remove(file)
                    print("删除文件: " + file + "成功")
                except Exception as e:
                    print(e)
                    print("删除文件失败 : " + file)

# 判断工作路径是否包含指定文件
def containFile(file):
    files = getPath()
    if files == None:
        True
    for i in files:
        if i .__contains__(file) :
            return False
    return True


def getTargetExcle(excles):
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    weekday = datetime.datetime.now().weekday()
    if excles == None:
        return
    for i in excles:
        if i.__contains__(now + "(" + handleFile.getWeekDayName(weekday) + ")" + "--"):
            return i
def removePath(path):
    try:
        for file in path:
            os.remove(file)
        print("清除文件成功!!!")
    except Exception as e:
        print(e)
        print("删除文件失败!!!")
if __name__ == "__main__":
    removeWeekFile()