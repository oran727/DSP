import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


from test_cao import *     #直接调出demo1，实现界面与业务逻辑的分离


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
