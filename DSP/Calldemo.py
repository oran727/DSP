import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtMultimedia import QSound
import scipy.io
from demo1 import *  # 直接调出demo1，实现界面与业务逻辑的分离
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import wave
import soundfile  # 这个库用来写入滤波后的音频信号
import matplotlib

matplotlib.use('Qt5Agg')  # 连接后端与前端（很重要）
matplotlib.rcParams['font.family'] = 'STSong  '  # 使标题可用宋体输出

# from matplotlib.patches import Circle  #零极点画单位圆，效果不佳，先注释


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        self.flieCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

        self.pushButton.clicked.connect(self.player)
        self.pushButton_2.clicked.connect(self.Time_frequency)  # 绘出音频的时域谱和频谱

        self.pushButton_3.clicked.connect(self.iir)  # 按动按钮设计IIR滤波器
        self.pushButton_4.clicked.connect(self.iirFilter)  # 按动按钮用IIR滤波器进行滤波
        self.pushButton_11.clicked.connect(self.iirZPK)  # 零极点
        self.pushButton_13.clicked.connect(self.iirGruopDelay)
        self.pushButton_5.clicked.connect(self.compareIIR)  # 按动按钮将滤波前的图像和IIR滤波后的图像放在一起比较
        self.pushButton_6.clicked.connect(self.outputWaviir)  # 将滤波后的波形转化回wav文件

        self.pushButton_7.clicked.connect(self.fir)  # 按动按钮设计FIR滤波器
        self.pushButton_8.clicked.connect(self.firFilter)  # 按动按钮用FIR滤波器进行滤波
        self.pushButton_12.clicked.connect(self.firZPK)  # 零极点
        self.pushButton_14.clicked.connect(self.firGruopDelay)
        self.pushButton_9.clicked.connect(self.compareFIR)  # 按动按钮将滤波前的图像和FIR滤波后的图像放在一起比较
        self.pushButton_10.clicked.connect(self.outputWavfir)  # 将滤波后的波形转化回wav文件

        self.lineEdit_6.setVisible(False)  # 首先设置IRR滤波器所需的fp2和fst2为不可见状态
        self.lineEdit_7.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)

        self.lineEdit_10.setVisible(False)  # 设置设计FIR所需的滤波器参数为不可见状态
        self.label_15.setVisible(False)
        self.lineEdit_12.setVisible(False)
        self.label_19.setVisible(False)

        self.checkBox_4.stateChanged.connect(self.lineEdit_6.setVisible)  # 当点击带通或带阻滤波时fp2和fst2可见
        self.checkBox_4.stateChanged.connect(self.lineEdit_7.setVisible)
        self.checkBox_4.stateChanged.connect(self.lineEdit_10.setVisible)
        self.checkBox_4.stateChanged.connect(self.lineEdit_12.setVisible)
        self.checkBox_4.stateChanged.connect(self.label_6.setVisible)
        self.checkBox_4.stateChanged.connect(self.label_7.setVisible)
        self.checkBox_4.stateChanged.connect(self.label_15.setVisible)
        self.checkBox_4.stateChanged.connect(self.label_19.setVisible)

        self.checkBox_3.stateChanged.connect(self.lineEdit_6.setVisible)
        self.checkBox_3.stateChanged.connect(self.lineEdit_7.setVisible)
        self.checkBox_3.stateChanged.connect(self.lineEdit_10.setVisible)
        self.checkBox_3.stateChanged.connect(self.lineEdit_12.setVisible)
        self.checkBox_3.stateChanged.connect(self.label_6.setVisible)
        self.checkBox_3.stateChanged.connect(self.label_7.setVisible)
        self.checkBox_3.stateChanged.connect(self.label_15.setVisible)
        self.checkBox_3.stateChanged.connect(self.label_19.setVisible)

    def openMsg(self):  # 控制音频文件的打开
        self.file, ok = QFileDialog.getOpenFileName(self, "打开", "音频文件", "(*.wav)")  # 打开文件

    def player(self):    #播放音频
        try:
            self.sound = QSound.play(self.file)
        except Exception:
            QMessageBox.critical(self, "错误", "没有打开音频文件！")

    def Time_frequency(self):
        try:
            path = self.file  # 将打开的文件传递到本函数
            wavfile = wave.open(path, "rb")
        except Exception:
           QMessageBox.critical(self,"错误","没有打开音频文件！")
        try:
            params = wavfile.getparams()
            # 一次性返回所有的音频参数，返回的是一个元组,包括声道数，量化位数(byte单位)，采样频率，采样点数
            nchannels, sampwidth, framesra, frameswav = params[:4]
            self.datawav = wavfile.readframes(frameswav)
            wavfile.close()
            self.datause = np.fromstring(self.datawav, dtype=np.short)  # 将字符串转换为数组，得到一维的short类型的数组

            self.time = np.arange(0, frameswav) * (1.0 / framesra)  # 赋值的归一化

            print(params)  # 在后台输出音频参数

            self.c = np.fft.fft(self.datause)  # 进行快速傅里叶变换
            self.c = abs(self.c)

            self.freq = np.arange(0, len(self.c))  # 建立时间轴

            fig, ax = plt.subplots(2, 1)

            ax[0].plot(self.time, self.datause)  # 画出时域图像
            ax[0].set_title("音频文件的时域图像")
            ax[0].set_xlabel('时间 /s')
            ax[0].set_ylabel('振幅 ')

            ax[1].plot(self.freq / 5, abs(self.c), color='red')  # 画出频域图像
            ax[1].set_xlim(0,4000)
            ax[1].set_title("音频文件的频域图像")
            ax[1].set_xlabel('频率 /Hz')
            ax[1].set_ylabel('幅值')

            plt.show()
        except:
            QMessageBox.critical(self, "错误", "音频文件的格式错误！")

    def iir(self):
        # 将gui中读取到的数值调用到这里设计滤波器
        try:
            f = float(self.lineEdit.text())  # 抽样频率，已经在gui中设置了默认值为8000
            gpass = float(self.lineEdit_2.text())
            gstop = float(self.lineEdit_3.text())

            # 下面加入条件判断，因为低通或高通滤波器只需要一组数据，而带通、带阻滤波器需要两组
            # 通带频率和阻带频率，如果是带通或者带阻滤波器，这里要两组数据
            if self.checkBox_3.isChecked() or self.checkBox_4.isChecked():
                fp1 = float(self.lineEdit_4.text())
                fst1 = float(self.lineEdit_5.text())
                fp2 = float(self.lineEdit_6.text())
                fst2 = float(self.lineEdit_7.text())
                wp = [2 * fp1 / f, 2 * fp2 / f]
                ws = [2 * fst1 / f, 2 * fst2 / f]

            # 低通、高通滤波用这里，只要一组数据
            if self.checkBox.isChecked() or self.checkBox_2.isChecked():
                fp1 = float(self.lineEdit_4.text())
                fst1 = float(self.lineEdit_5.text())
                wp = (2 * fp1) / f
                ws = (2 * fst1) / f

            iirType = self.comboBox.currentText()  # 在comboBox中选择想要的滤波器类型

            self.b, self.a = signal.iirdesign(wp, ws, gpass, gstop, False, iirType, "ba")  # 根据选择的滤波器类型，返回分子分母形式
            self.z1, self.p1, self.k1 = signal.iirdesign(wp, ws, gpass, gstop, False, iirType, "zpk")  # 返回零极点
            self.w1, self.gd1 = signal.group_delay((self.b, self.a))  # 计算群延迟

            w, h = signal.freqz(self.b, self.a)  # 计算滤波器的频率响应

            plt.figure()
            plt.plot(w * f / (2 * np.pi), np.abs(h))
            plt.title('IIR数字滤波器')
            plt.ylabel('衰减')
            plt.xlabel('频率')
            plt.show()

        except Exception:
            QMessageBox.critical(self, "错误", "请正确输入滤波器相关参数！")

    def iirZPK(self):  # 绘出零极点
        try:
            fig, ax = plt.subplots()
            # circle = Circle(xy=(0.0, 0.0), radius=1, alpha=0.9)
            # ax.add_patch(circle)

            for i in self.p1:
                ax.plot(np.real(i), np.imag(i), 'bx')  # pole before quantization
            for i in self.z1:
                ax.plot(np.real(i), np.imag(i), 'bo')  # pole before quantizatio
            ax.set_title('零极点分布（o代表零点，x代表极点）')
            plt.show()
        except Exception:
            QMessageBox.critical(self,"错误","请先设计IIR滤波器！")

    def iirGruopDelay(self):  # 绘出群延迟
        try:
            plt.plot(self.w1, self.gd1)
            plt.title("IIR滤波器的群延迟")
            plt.xlabel("频率  [rad/sample]")
            plt.ylabel('群延迟')
            plt.show()
        except Exception:
            QMessageBox.critical(self,"错误","请先设计IIR滤波器！")

    def fir(self):
        try:
            global f, type, N
            firWindows = str(self.comboBox_2.currentText())  # 获取fir滤波器的窗口类型
            fs = float(self.lineEdit_8.text())  # 抽样频率

            if self.checkBox.isChecked():  # 低通滤波
                f = float(self.lineEdit_9.text())  # 通带截止频率
                fst = float(self.lineEdit_11.text())  # 阻带截止频率
                w = 2 * (fst - f) / fs
                f = 2 * f / fs
                type = 'lowpass'

                if self.comboBox_2.currentText() == 'boxcar':  # 矩形窗
                    N = 1.8 / w
                    N = int(N)
                    if N % 2 == 0:  # 如果是偶数要转化成奇数
                        N = N + 1

                elif self.comboBox_2.currentText() == "triang":  # 三角形窗
                    N = 6.1 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hann":  # 汉宁窗
                    N = 6.2 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hamming":  # 海明窗
                    N = 6.6 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "blackmanharris":  # 布莱克曼窗
                    N = 11 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                numtaps =  N  # 将算出的阶数传递
                numtaps = int(numtaps)


            if self.checkBox_2.isChecked():  # 高通滤波
                f = float(self.lineEdit_9.text())  # 通带截止频率
                fst = float(self.lineEdit_11.text())  # 阻带截止频率
                w = 2 * (f - fst) / fs
                f = 2 * fst / fs
                type = 'highpass'

                if self.comboBox_2.currentText() == 'boxcar':  # 矩形窗
                    N = 1.8 / w
                    N = int(N)
                    if N % 2 == 0:  # 如果是偶数要转化成奇数
                        N = N + 1

                elif self.comboBox_2.currentText() == "triang":  # 三角形窗
                    N = 6.1 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hann":  # 汉宁窗
                    N = 6.2 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hamming":  # 海明窗
                    N = 6.6 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "blackmanharris":  # 布莱克曼窗
                    N = 11 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                numtaps = N  # 将算出的阶数传递
                numtaps = int(numtaps)

            if self.checkBox_3.isChecked():  # 带通滤波
                #f = [f1, f2]
                type = 'bandpass'
                fp1 = float(self.lineEdit_9.text())
                fp2 = float(self.lineEdit_10.text())
                fst1 = float(self.lineEdit_11.text())
                fst2 = float(self.lineEdit_12.text())
                w1 = 2 * (fp1 - fst1) / fs
                w2 = 2 * (fst2 - fp2) / fs
                f = [2 * fp1 /fs, 2 *fp2 / fs]

                # 取两者之中的较小者作为过度带宽
                if w2 < w1:
                    w = w2
                else:
                    w = w1

                if self.comboBox_2.currentText() == 'boxcar':  # 矩形窗
                    N = 1.8 / w
                    N = int(N)
                    if N % 2 == 0:  # 如果是偶数要转化成奇数
                        N = N + 1

                elif self.comboBox_2.currentText() == "triang":  # 三角形窗
                    N = 6.1 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hann":  # 汉宁窗
                    N = 6.2 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hamming":  # 海明窗
                    N = 6.6 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "blackmanharris":  # 布莱克曼窗
                    N = 11 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                numtaps = N  # 将算出的阶数传递
                numtaps = int(numtaps)

            if self.checkBox_4.isChecked():  # 带阻滤波
                type = 'bandstop'
                fp1 = float(self.lineEdit_9.text())
                fp2 = float(self.lineEdit_10.text())
                fst1 = float(self.lineEdit_11.text())
                fst2 = float(self.lineEdit_12.text())
                w1 = 2 * (fst1 - fp1) / fs
                w2 = 2 * (fp2 - fst2) / fs
                f = [2 * fst1 /fs, 2 *fst2 / fs]

                # 取两者之中的较小者作为过度带宽
                if w2 < w1:
                    w = w2
                else:
                    w = w1

                if self.comboBox_2.currentText() == 'boxcar':  # 矩形窗
                    N = 1.8 / w
                    N = int(N)
                    if N % 2 == 0:  # 如果是偶数要转化成奇数
                        N = N + 1

                elif self.comboBox_2.currentText() == "triang":  # 三角形窗
                    N = 6.1 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hann":  # 汉宁窗
                    N = 6.2 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "hamming":  # 海明窗
                    N = 6.6 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                elif self.comboBox_2.currentText() == "blackmanharris":  # 布莱克曼窗
                    N = 11 / w
                    N = int(N)
                    if N % 2 == 0:
                        N = N + 1

                numtaps = N  # 将算出的阶数传递
                numtaps = int(numtaps)

            self.FIR = signal.firwin(numtaps, f, window=firWindows, pass_zero=type)  #将相关参数传递到此处设计FIR滤波器
            w, h = signal.freqz(self.FIR)

            plt.figure()
            plt.plot(w* fs / (2 * np.pi), np.abs(h))
            plt.title('FIR数字滤波器')
            plt.ylabel('衰减')
            plt.xlabel('频率')
            plt.show()
        except:
            QMessageBox.critical(self, "错误", "请正确输入滤波器相关参数！")

    def firZPK(self):  # 绘出零极点
        try:
            fig, ax = plt.subplots()
            # circle = Circle(xy=(0.0, 0.0), radius=1, alpha=0.9)
            # ax.add_patch(circle)

            a = 1  # 令分母为1
            self.z2, self.p2, self.k2 = signal.tf2zpk(self.FIR, a)
            for i in self.p2:
                ax.plot(np.real(i), np.imag(i), 'bx')  # pole before quantization
            for i in self.z2:
                ax.plot(np.real(i), np.imag(i), 'bo')  # pole before quantizatio
            ax.set_title('零极点分布（o代表零点，x代表极点）')
            plt.show()
        except:
            QMessageBox.critical(self,"错误","请先设计FIR滤波器！")

    def firGruopDelay(self):  # 绘出群延迟
        try:
            self.w2, self.gd2 = signal.group_delay(self.FIR, 1)

            plt.figure()
            plt.plot(self.w2, self.gd2)
            plt.title("FIR滤波器的群延迟")
            plt.xlabel("频率  [rad/sample]")
            plt.ylabel('群延迟')
            plt.show()
        except:
            QMessageBox.critical(self,"错误","请先设计FIR滤波器！")

    def iirFilter(self):  # 用设计出来的滤波器对音频进行滤波
        try:
            self.y = signal.lfilter(self.b, self.a, self.datause)  # 用设计出来的滤波器对音频进行滤波
            self.Y = np.fft.fft(self.y)  # 进行快速傅里叶变换 ,求频域

            plt.figure()
            plt.subplot(211)
            plt.title("滤波后的时域图像")
            plt.ylabel("振幅")
            plt.xlabel("时间 /s")
            plt.plot(self.time, self.y)

            plt.subplot(212)
            plt.title("滤波后的频域图像")
            plt.ylabel("幅度")
            plt.xlabel("频率 /Hz")
            plt.xlim(0,4000)
            plt.plot(self.freq/5, abs(self.Y), color='red')
            plt.show()
        except:
            QMessageBox.critical(self,"错误","没有打开音频文件或没有设计滤波器！")

    def firFilter(self):
        try:
            a = 1  # 分母为1
            self.z = signal.lfilter(self.FIR, a, self.datause)  # 用设计出来的滤波器对音频进行滤波
            self.Z = np.fft.fft(self.z)

            plt.figure()
            plt.subplot(211)
            plt.title("滤波后的时域图像")
            plt.ylabel("振幅")
            plt.xlabel("时间 /s")
            plt.plot(self.time, self.z)

            plt.subplot(212)
            plt.title("滤波后的频域图像")
            plt.ylabel("幅度")
            plt.xlabel("频率 /Hz")
            plt.xlim(0,4000)
            plt.plot(self.freq /5, abs(self.Z), color='red')

            plt.show()
        except:
            QMessageBox.critical(self,"错误","没有打开音频文件或没有设计滤波器！")

    def compareIIR(self):
        try:
            plt.figure()

            plt.subplot(221)
            plt.title("音频文件的时域图像")
            plt.ylabel("振幅")
            plt.xlabel("时间 /s")
            plt.plot(self.time, self.datause)

            plt.subplot(222)
            plt.title("音频文件的频域图像")
            plt.ylabel("幅度")
            plt.xlabel("频率 /Hz")
            plt.xlim(0,4000)
            plt.plot(self.freq/5, abs(self.c), color='red')

            plt.subplot(223)
            plt.title("滤波后的时域图像")
            plt.ylabel("振幅")
            plt.xlabel("时间 /s")
            plt.plot(self.time, self.y)

            plt.subplot(224)
            plt.title("滤波后的频域图像")
            plt.ylabel("幅度")
            plt.xlabel("频率 /Hz")
            plt.xlim(0,4000)
            plt.plot(self.freq/5, abs(self.Y), color='red')
            plt.show()
        except:
            QMessageBox.critical(self,"错误","没有打开音频文件或没有设计滤波器！")

    def compareFIR(self):
        try:
            plt.figure()

            plt.subplot(221)
            plt.title("音频文件的时域图像")
            plt.ylabel("振幅")
            plt.xlabel("时间 /s")
            plt.plot(self.time, self.datause)

            plt.subplot(222)
            plt.title("音频文件的频域图像")
            plt.ylabel("幅度")
            plt.xlabel("频率 /Hz")
            plt.xlim(0,4000)
            plt.plot(self.freq/5, abs(self.c), color='red')

            plt.subplot(223)
            plt.title("滤波后的时域图像")
            plt.ylabel("振幅")
            plt.xlabel("时间 /s")
            plt.plot(self.time, self.z)

            plt.subplot(224)
            plt.title("滤波后的频域图像")
            plt.ylabel("幅度")
            plt.xlabel("频率 /Hz")
            plt.xlim(0,4000)
            plt.plot(self.freq/5, abs(self.Z), color='red')
            plt.show()
        except:
            QMessageBox.critical(self,"错误","没有打开音频文件或没有设计滤波器！")

    def outputWaviir(self):
        try:
            self.y = self.y.astype(np.short)  # 经过滤波后的数据是float类型，要重新声明为short类型
            freq = int(self.lineEdit.text())
            soundfile.write("noise/Iirwav.wav", self.y, freq)
            filename = "noise/Iirwav.wav"
            self.sound = QSound.play(filename)
        except:
            QMessageBox.critical(self,"错误","请先进行滤波！")

    def outputWavfir(self):
        try:
            self.z = self.z.astype(np.short)
            freq = int(self.lineEdit_8.text())
            soundfile.write("noise/Firwav.wav", self.z, freq)
            filename = "noise/Firwav.wav"
            self.sound = QSound.play(filename)
        except:
            QMessageBox.critical(self,"错误","请先进行滤波！")



# 开始主循环
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
