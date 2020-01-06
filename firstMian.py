import sys
from  PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class IconForm1(QMainWindow):  # 从主窗口继承
    # 将相关的初始化方法都写在同一个初始化方法里
    def __init__(self):
        super(IconForm1,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('设置宽口图标')
        # self.setGeometry(300,300,200,200)  # 同时设置窗口坐标（300，300），窗口大小（200，200）
        self.setWindowIcon(QIcon('./1.ico'))  # 图标文件为当前目录下1.ico
        self.resize(400,300)
        self.status=self.statusBar()  # 设置状态栏
        self.status.showMessage('只存在5秒的信息',5000)  # 设置显示的消息，存在时间为5000毫秒


if __name__=='__main__':
    app=QApplication(sys.argv)
    # app.setWindowIcon(QIcon(r'D:\BrowserDownload\1.icon'))
    main=IconForm1()  # 创建类的实例
    main.show()
    sys.exit(app.exec())


