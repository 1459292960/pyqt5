import sys
from PyQt5.QtWidgets import QApplication,QWidget,QComboBox,QHBoxLayout,QLabel

class comboBoxDemo(QWidget):
    def __init__(self):
        super(comboBoxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('下拉列表框测试')

        self.label=QLabel('请选择您最喜欢的春节晚会节目')
        layout=QHBoxLayout()  # 使用水平布局
        self.cb=QComboBox()  # 实例化一个下拉列表框
        self.cb.addItems(['相声','小品','歌曲','舞蹈'])  # 添加下拉列表中的选项
        self.cb.currentIndexChanged.connect(self.selectionChange)  # 信号绑定，并传递所选的索引Index
        # 控件使用水平布局
        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)
    def selectionChange(self,i):
        "这是一个函数文档，下面的for循环及那个cb下拉列表框中的项都打印出来"
        for count in range(self.cb.count()):
            print('item'+str(count)+'='+self.cb.itemText(count))
        # 打印目前选中的
        print('current index',i,'selection changed',self.cb.currentText())
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=comboBoxDemo()
    main.show()
    sys.exit(app.exec_())


