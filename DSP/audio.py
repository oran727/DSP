import os
import wave
import numpy as np
import matplotlib.pyplot as plt

# 1、批量读取.wav文件名：
filepath = "noise/sound_Lnoise.wav"


# for file in  filename:
#print(filename[50])
# #打开一个声音文件，，返回一个声音的实例

f = wave.open(filepath)
# #获取wav文件的参数（以tuple形式输出），依次为(声道数，采样精度，采样率，帧数，......)
# 返回的是一个组元
params = f.getparams()
# # 获取前几个参数
nchannels, sampwidth, framerate, nframes = params[:4]
# 读取音频，字符串格式
# 得到每一帧的声音数据，返回的值是二进制数据，
# 在python中用字符串表示二进制数据，如下图，所以我们后面要进行转化.
strData = f.readframes(nframes)
f.close()

# #将波形数据字符串转为int类型
# 接下来需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组：

waveData = np.fromstring(strData, dtype=np.short)

waveData.shape = -1, 2
waveData = waveData.T

time = np.arange(0, nframes) * (1.0 / framerate)

plt.subplot(211)
plt.plot(time, waveData[0])
plt.subplot(212)
plt.plot(time, waveData[1], c="g")

plt.xlabel('Time(s)')
plt.ylabel("Amplitude")
plt.title("Single channel wavedata")
plt.grid('on')  # 标尺，on：有，off:无。
plt.show()