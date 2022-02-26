#wave data   -xlxw

from scipy import signal
import wave
import numpy as np
import matplotlib.pyplot as plt
import sys

wp = 0.2
ws = 0.3
gpass = 1
gstop = 40
b,a = signal.iirdesign(wp,ws,gpass,gstop,False,"ellip","ba")  #采用椭圆型方法，返回分子分母形式
z,p,k = signal.iirdesign(wp,ws,gpass,gstop,False,"ellip","zpk")  #返回零极点
w, gd = signal.group_delay((b, a))  # 计算群延迟

w,h = signal.freqz(b,a)



wavfile =  wave.open("noise/sound_Hnoise.wav","rb")

params = wavfile.getparams()
#一次性返回所有的音频参数，返回的是一个元组,包括声道数，量化位数(byte单位)，采样频率，采样点数
nchannels, sampwidth, framesra, frameswav = params[:4]
datawav = wavfile.readframes(frameswav)
wavfile.close()
datause = np.fromstring(datawav,dtype = np.short)
datause = datause.astype(np.short)
time = np.arange(0, frameswav) * (1.0/framesra)
print(framesra)


N=len(datause)

c=np.fft.fft(datause)

Freq = np.arange(0, len(c))

y= signal.lfilter(b,a,datause)


print(datause)
print(c)


fig, ax = plt.subplots(2, 1)


ax[0].plot(time,datause,color = 'green')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')


ax[1].plot(time ,y,color = 'red')
ax[1].set_xlabel('Freq(HZ)')
ax[1].set_ylabel('Y(freq)')

plt.show()



