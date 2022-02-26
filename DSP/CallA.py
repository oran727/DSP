import sys
import matplotlib  # 解决中文显示问题
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from PyQt5.QtWidgets import QMainWindow, QApplication
from A import *
from PyQt5.QtWidgets import *

matplotlib.use('Qt5Agg')
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 创建一个类
class design(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(design, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.irr)


    def irr(self):
        #wp = float(self.lineEdit.text())
        #ws = float(self.lineEdit_2.text())
        gpass = float(self.lineEdit_3.text())
        gstop = float(self.lineEdit_4.text())
        f = float(self.lineEdit_7.text())
        #低通、高通滤波器，只要一组数据
        if self.checkBox.isChecked() or self.checkBox_2.isChecked():
            fp1 = float(self.lineEdit.text())
            fs1 = float(self.lineEdit_2.text())
            wp = (2 * fp1) / f
            ws = (2 * fs1) / f
        if self.checkBox_3.ischecked() or self.checkBox_4.ischecked():
            fp1 = float(self.lineEdit.text())
            fs1 = float(self.lineEdit_2.text())
            fp2 = float(self.lineEdit_5.text())
            fs2 = float(self.lineEdit_6.text())
            wp = [2 * fp1 / f, 2 * fp2 / f]
            ws = [2 * fs1 / f, 2 * fs2 / f]

        irrtype=self.comboBox.currentText()
        self.b, self.a = signal.iirdesign(wp, ws, gpass, gstop, False,irrtype)
        (w, h) = signal.freqz(self.b, self.a)  #计算滤波器的频率响应
        plt.figure()
        plt.plot(w*f/(2*np.pi), np.abs(h))
        plt.title("IIR数字滤波器")
        plt.ylabel('衰减')
        plt.xlabel('频率')
        plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = design()
    win.show()
    sys.exit(app.exec_())
