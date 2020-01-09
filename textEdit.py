from sys import argv,exit
from  PyQt5.QtWidgets import QApplication,QMainWindow,QTextEdit,QPushButton,QVBoxLayout,QWidget,QLineEdit
from time import sleep
class textEditDemo(QMainWindow):
    def __init__(self):
        super(textEditDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本框演示')
        layout=QVBoxLayout()

        self.text=QTextEdit()
        layout.addWidget(self.text)
        self.line=QLineEdit()
        layout.addWidget(self.line)
        self.line.setReadOnly(True)
        self.line.setText('只可读')


        self.btn1=QPushButton('获取文本')
        self.btn1.clicked.connect(self.onClicked)
        layout.addWidget(self.btn1)
        self.btn2=QPushButton('进度显示')
        self.btn2.clicked.connect(self.Process)
        layout.addWidget(self.btn2)

        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
    def Process(self):
        width1=10
        n_max=100
        for n in range(1,n_max+1):
            left=int(n/n_max*width1)
            right=width1-left
            percent=n/n_max*100
            self.text.clear()  # 将textEdit组件里的内容全部删除
            # 将内容显示在text组件中
            self.text.setPlainText('Processing:'+'['+'#'*left+' '*right+']'+f'{percent:.0f}%\n')
            # 将进度条实时显示出来，否则会等到最后结果才显示
            QApplication.processEvents()
            sleep(0.5)  # 延时0.5s


    def onClicked(self):
        # 获取text组件中的内容
        print(self.text.toPlainText())
if __name__=='__main__':
    app=QApplication(argv)
    main=textEditDemo()
    main.show()
    exit(app.exec_())

