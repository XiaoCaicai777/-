import sys
from PySide2 import QtGui


class Message(QtGui.QWidget):

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
        # Are you sure to quit?窗口显示内容
        # QtGui.QMessageBox.Yes | QtGui.QMessageBox.No窗口按钮部件
        # QtGui.QMessageBox.No默认焦点停留在NO上
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?",
                                           QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        # 判断返回结果处理相应事项
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()