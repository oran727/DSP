import numpy as np
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib
import math
import matplotlib.ticker
from matplotlib.patches import Circle




matplotlib.rcParams['font.family']='STSong  '#使标题可用宋体输出


# Fs = input("请输入抽样频率：")
# fp = input("请输入通带截止频率：")
# fs = input("请输入阻带截止频率：")  # 获取滤波器相关参数
#
#
#
# wp = (2 * math.pi * float(fp))/float(Fs)
# ws = (2 * math.pi * float(fs))/float(Fs)        #数字化临界频率

# N,Wn = signal.buttord(wp,ws,1,15) #返回滤波器的阶数
#
# b,a = signal.butter(N,Wn)   #设计巴特沃斯低通滤波器
#
# w,h =signal.freqz(b,a)     #下面尝试用IIR design方法设计

f= 8000    #抽样频率为8000
fp = 1000
fs = 1500

wp = (2 * fp ) / f

ws = (2 * fs ) /f


gpass = 1
gstop = 40
b,a = signal.iirdesign(wp,ws,gpass,gstop,False,"ellip","ba")  #采用椭圆型方法，返回分子分母形式
z,p,k = signal.iirdesign(wp,ws,gpass,gstop,False,"ellip","zpk")  #返回零极点
w, gd = signal.group_delay((b, a))  # 计算群延迟

w,h = signal.freqz(b,a)

'''fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
ax1.grid()
ax1.set_ylim([-120, 20])

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid()
ax2.axis('tight')
ax2.set_ylim([-6, 1])
ax2.set_xlim([0,3])'''

plt.plot(w, np.abs(h))
plt.title('数字滤波器')
plt.ylabel('衰减')
plt.xlabel('频率')
plt.show()

# plt.plot(np.real(p), np.imag(p), 'x', label=u"极点分布")

fig, ax = plt.subplots()
circle = Circle(xy = (0.0, 0.0), radius = 1, alpha = 0.9)
ax.add_patch(circle)

for i in p:
    ax.plot(np.real(i),np.imag(i), 'bx')    #pole before quantization
for i in z:
    ax.plot(np.real(i),np.imag(i), 'bo')    #pole before quantization

ax.set_xlim(-1.8,1.8)
ax.set_ylim(-1.2,1.2)
ax.grid()
plt.show()

print("零点是：" , z)
print("极点是：", p)
print("系统增益是：", k)

