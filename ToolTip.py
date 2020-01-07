import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip,QPushButton,QVBoxLayout,QWidget

class ToolTip1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 鼠标停留整个界面（除控件外）都会弹出的提示消息
        self.setToolTip('<b>今天</b>是个好日子')
        self.setWindowTitle('设置提示消息')
        # 指定btn1的提示消息
        self.btn1=QPushButton('点我呀')
        self.btn1.setToolTip('按了也没用，哈哈')
        self.btn2=QPushButton('点我试试')
        self.btn2.setToolTip('点了也没用，嘻嘻')
        # 使用垂直布局
        layout=QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        # 所有控件放在QWidget上面，其其布局采用上面的layout布局
        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        # 将mainFrame 放在整个界面窗口上
        self.setCentralWidget(mainFrame)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ToolTip1()
    main.show()
    sys.exit(app.exec_())