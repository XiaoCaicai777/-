import sys
import threading

import PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PySide2.QtGui import QIcon
import re
import getFruitTest
from threading import Thread
import inspect, ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class Message(PySide2.QtWidgets.QMainWindow):

    def __init__(self):
        # 如果希望窗口内嵌于其他部件，可添加parent参数
        super(Message, self).__init__()
        # 调用初始化方法
        self.initUI()

    def initUI(self):
        # 设置窗口的所在位置，以左上角为原点，x轴300, y轴300, 宽250, 长150
        self.setGeometry(300, 310, 500, 250)
        # 给窗口一个标题名，你将会在标题栏看到这个名字
        self.setWindowTitle('小助手')

    def closeEvent(self, event):
        # message为窗口标题
        reply = QMessageBox.question(self, 'Message',
                                     "确定退出小助手吗?",
                                     QMessageBox.Yes |
                                     QMessageBox.No,
                                     QMessageBox.No)
        # 判断返回结果处理相应事项
        if reply == QMessageBox.Yes:
            if thread.is_alive():
                stop_thread(thread)
            sys.exit()
        else:
            event.ignore()


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


# '/^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/'
def handle(flag):
    if flag:
        info = textEdit.toPlainText()
        email = info.split(',')
        patter = "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$"
        for i in email:
            if not re.match(patter, i):
                QMessageBox.about(window, "错误提示", "请输入正确的邮箱， 用英文逗号隔开！！！！")
                return
        state = QMessageBox.question(window, "确认设置", '''设置的邮箱为： ''' + str(email), QMessageBox.No | QMessageBox.Yes,
                                 QMessageBox.No)
        if state == QMessageBox.Yes:
            file = open("email_config.dls", "wb+")
            try:
                if file.write(info.encode()) > 0:
                    file.close()
            except Exception as e:
                file.close()
                print(e)
            else:
                pass
    if not Thread.is_alive(thread):
        thread.start()

def exitAppHandle():
    # message为窗口标题
    reply = QMessageBox.question(window, 'Message',
                                 "确定退出小助手吗?",
                                 QMessageBox.Yes |
                                 QMessageBox.No,
                                 QMessageBox.No)
    # 判断返回结果处理相应事项
    if reply == QMessageBox.Yes:
        if thread.is_alive():
            stop_thread(thread)
        app.exit()
        sys.exit()
    else:
        pass

if __name__ == '__main__':
    app = QApplication([])

    # 设置icon
    app.setWindowIcon(QIcon('./小助手.jpg'))

    window = Message()
    # # 窗口大小
    # window.resize(500, 250)
    #
    # # 初始化时， 窗口相对屏幕的位置 单位是px
    # window.move(300, 310)
    # 窗口名字
    # window.setWindowTitle("小助手")

    textEdit = QPlainTextEdit(window)
    textEdit.setPlaceholderText("如需修改收件邮箱， 请输入新收件邮箱,用逗号隔开！！！")

    # 输入框相对窗口位置
    textEdit.move(10, 25)
    textEdit.resize(300, 150)

    # 输入框相对窗口位置
    button = QPushButton("确认", window)
    button.move(380, 50)

    sendButton = QPushButton("发送", window)
    sendButton.move(200, 200)

    # 输入框相对窗口位置
    exitApp = QPushButton("退出", window)
    exitApp.move(380, 120)

    exitApp.clicked.connect(exitAppHandle)

    # 处理点击事件
    button.clicked.connect(lambda: handle(True))

    sendButton.clicked.connect(lambda: handle(False))
    # 展现在界面上
    window.show()
    thread = Thread(target=getFruitTest.main)
    # thread = Thread(target=exitAppHandle)
    sys.exit(app.exec_())
