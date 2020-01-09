import sys
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QRadioButton,QWidget

class QRadioDemo(QWidget):
    def __init__(self):
        super(QRadioDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('radiobutton测试')
        layout=QHBoxLayout()

        self.btn1=QRadioButton('单选按钮1')
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda :self.buttonState(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2=QRadioButton('单选按钮2')
        # 使用lambda 表达式传递参数，神奇
        self.btn2.toggled.connect(lambda:self.buttonState(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)

    def buttonState(self,btn):
        if btn.isChecked()==True:
             print(btn.text()+'被勾选')
        else:
            None
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QRadioDemo()
    main.show()
    sys.exit(app.exec_())


