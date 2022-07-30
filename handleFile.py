import datetime

def getWeekDayName(weekday):
    if weekday==0:
        return "周一"
    if weekday==1:
        return "周二"
    if weekday==2:
        return "周三"
    if weekday==3:
        return "周四"
    if weekday==4:
        return "周五"
    if weekday==5:
        return "周六"
    if weekday==6:
        return "周日"

def getDatePath(flag):
    excleFiles = []
    for i in range(0,7):
        date = (datetime.datetime.now() - datetime.timedelta(days=i)).date().strftime('%Y-%m-%d')
        weekday = (datetime.datetime.now() - datetime.timedelta(days=i)).date().weekday()
        if flag:
            excleFiles.append(date + "(" + getWeekDayName(weekday) + ")" + ".xls")
        else:
            excleFiles.append(date + "(" + getWeekDayName(weekday) + ")")
    return excleFiles

if __name__ == "__main__":
    getDatePath(False)