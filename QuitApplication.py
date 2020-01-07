import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QHBoxLayout,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()

        # 调用本（这个）类中的initUI方法
        self.initUI()
    def initUI(self):

        self.setWindowTitle('退出应用程序')
        self.btn1 = QPushButton('Quit')

        self.btn1.clicked.connect(self.onClick_Button)
        # 使用水平布局放置按钮
        layout=QHBoxLayout()
        layout.addWidget(self.btn1)
        # 所有的控件都放在QWidget上
        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        # 将主框架放在整个界面窗口上
        self.setCentralWidget(mainFrame)


    def onClick_Button(self):
        sender=self.sender()
        # sender.text() 获取与onClick_Button绑定的信号btn1上的文本
        print(sender.text()+'我被按下啦')
        app=QApplication.instance()
        app.quit()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QuitApplication()
    main.show()
    sys.exit(app.exec_())

