from sys import argv,exit
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QGridLayout,QLabel,QMainWindow
from PyQt5.QtGui import QDoubleValidator

class lineEditDemo(QMainWindow):
    ' 在不知道用途的情况下用QWidget，需要菜单栏、工具栏、状态栏使用QMainWindow，文件对话框/消息对话框用QDialog '
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()
    def initUI(self):
        bar=self.menuBar()
        file=bar.addMenu('文件')
        tool_help=file.addMenu('帮助')  # 在文件菜单下再建一个子菜单项'帮助'
        tool_help.addAction('技术支持')
        quit=file.addAction('退出')
        quit.triggered.connect(self.Quit)


        grid=QGridLayout()  # 使用栅格布局
        self.label1=QLabel('浮点数校验：')  # 实例化一个QLabel组件，并将其上文字显示为 '浮点数校验：'
        grid.addWidget(self.label1,0,0)  # 放置在第0行、第0列
        self.line1=QLineEdit()
        grid.addWidget(self.line1,0,1)
        self.line1.setPlaceholderText('浮点类型')  # 设置LineEdit未输入时的提示词

        self.line1.setValidator(QDoubleValidator())  # 使用浮点校验器（限制只能输入浮点数（包括整数））
        mainFrame=QWidget()
        mainFrame.setLayout(grid)
        self.setCentralWidget(mainFrame)
        # self.setLayout(grid)  # 将所有以grid栅格布局的控件都显示出来
    def Quit(self):
        app=QApplication.instance()
        app.quit()

if __name__=='__main__':
    '测试本程序正确性'
    app=QApplication(argv)
    main=lineEditDemo()
    main.show()
    exit(app.exec_())
