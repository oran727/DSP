import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QComboBox, QCheckBox
import matplotlib
import sys
matplotlib.rcParams['font.family'] = 'STSong  '  # 使标题可用宋体输出
matplotlib.use('Qt5Agg')
from demo3 import *

class design(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(design, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.irrFilter)
        self.pushButton_2.clicked.connect(self.irrGroup_Delay)

    def irrFilter(self):
        wp = float(self.lineEdit.text())
        ws = float(self.lineEdit_4.text())
        gpass = float(self.lineEdit_2.text())
        gstop = float(self.lineEdit_3.text())

        self.b, self.a = signal.iirdesign(wp, ws, gpass, gstop)
        w, h = signal.freqz(self.b, self.a)

        plt.figure()
        plt.plot(w, np.abs(h))
        plt.xlabel("归一化频率")
        plt.ylabel("衰减")
        plt.title("IIR数字滤波器")
        plt.show()

    def irrGroup_Delay(self):
        w1,gd = signal.group_delay((self.b,self.a))
        plt.figure()
        plt.plot(w1, gd)
        plt.title("群延迟")
        plt.show()


# 开始主循环
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = design()
    myWin.show()
    sys.exit(app.exec_())