import matplotlib.pyplot as plt
from scipy import signal
from PyQt5.QtWidgets import QApplication, QMainWindow
from test1 import *   #实现用户界面和业务逻辑的分离
import numpy as np
import sys
import matplotlib
matplotlib.use('Qt5Agg')   #连接后端与前端（很重要）
matplotlib.rcParams['font.family'] = 'STSong  '  # 使标题可用宋体输出


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.irrFilter)

    def irrFilter(self):
        wp = 0.2
        ws = 0.3
        gpass = 1
        gstop = 40

        b,a = signal.iirdesign(wp,ws,gpass,gstop)
        w,h = signal.freqz(b,a)

        plt.figure()
        plt.plot(w,np.abs(h))
        plt.xlabel("归一化频率")
        plt.ylabel("衰减")
        plt.title("IIR数字滤波器")
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Test()
    myWin.show()
    sys.exit(app.exec_())