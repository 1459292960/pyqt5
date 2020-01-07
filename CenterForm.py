import sys
from  PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon

class IconForm1(QMainWindow):  # 从主窗口继承
    # 将相关的初始化方法都写在同一个初始化方法里
    def __init__(self):
        super(IconForm1,self).__init__()
        self.initUI()
        self.center()
    def initUI(self):
        self.setWindowTitle('设置宽口图标')
        # self.setGeometry(300,300,200,200)  # 同时设置窗口坐标（300，300），窗口大小（200，200）
        # self.setWindowIcon(QIcon('./1.ico'))  # 图标文件为当前目录下1.ico
        self.resize(400,300)
        self.status=self.statusBar()  # 设置状态栏
        self.status.showMessage('只存在5秒的信息',5000)  # 设置显示的消息，存在时间为5000毫秒
    def center(self):
        # 获取当前显示器屏幕大小
        screen=QDesktopWidget().screenGeometry()
        # 获取当前应用窗口大小
        size=self.geometry()
        # 计算当前窗口左上角一点在屏幕坐标系的位置（以一点带动整个应用程序界面运动）
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        # 将界面移动到计算好的位置（屏幕中央）
        self.move(newLeft,newTop)



if __name__=='__main__':
    app=QApplication(sys.argv)
    # app.setWindowIcon(QIcon(r'D:\BrowserDownload\1.icon'))
    main=IconForm1()  # 创建类的实例
    main.show()
    sys.exit(app.exec())
