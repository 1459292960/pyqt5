import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QCheckBox,QWidget
'''
绑定
stateChanged
'''
class CheckBoxDemo(QMainWindow):
    def __init__(self):
        super(CheckBoxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('复选框测试')
        layout=QHBoxLayout()

        self.cb1=QCheckBox('复选框控件1')
        self.cb1.setChecked(True)
        self.cb1.stateChanged.connect(lambda : self.checkboxState(self.cb1))
        layout.addWidget(self.cb1)

        self.cb2=QCheckBox('复选框控件2')
        self.cb2.stateChanged.connect(lambda: self.checkboxState((self.cb2)))
        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
        layout.addWidget(self.cb2)

    def checkboxState(self,cb):
        cbStatus=cb.text()+',is Checked='+str(cb.isChecked())+',checkState='+str(cb.checkState())
        print(cbStatus+'\n')
        if self.cb2.isChecked()==True:
            print('想干啥干啥')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=CheckBoxDemo()
    main.show()
    sys.exit(app.exec_())
