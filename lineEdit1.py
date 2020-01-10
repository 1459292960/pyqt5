from sys import argv,exit
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QGridLayout,QLabel
from PyQt5.QtGui import QDoubleValidator

class lineEditDemo(QWidget):
    ' QWidget可以代替QMainWindow和QDialog '
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()
    def initUI(self):
        grid=QGridLayout()  # 使用栅格布局
        self.label1=QLabel('浮点数校验：')  # 实例化一个QLabel组件，并将其上文字显示为 '浮点数校验：'
        grid.addWidget(self.label1,0,0)  # 放置在第0行、第0列
        self.line1=QLineEdit()
        grid.addWidget(self.line1,0,1)
        self.line1.setPlaceholderText('浮点类型')  # 设置LineEdit未输入时的提示词

        self.line1.setValidator(QDoubleValidator())  # 使用浮点校验器（限制只能输入浮点数（包括整数））
        self.setLayout(grid)  # 将所有以grid栅格布局的控件都显示出来
if __name__=='__main__':
    '测试本程序正确性'
    app=QApplication(argv)
    main=lineEditDemo()
    main.show()
    exit(app.exec_())
