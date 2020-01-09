'''
dialog 最基本的对话框
调出来的对话框一切界面/控件都要自己添加，否则就是空白
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton,QDialog,QApplication,QMainWindow
class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(60,80)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        # 设置ApplicationModal:出现此子对话框时，原主对话框不可用
        dialog.setWindowModality(Qt.ApplicationModal)
        # 进入此子对话框主循环
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())