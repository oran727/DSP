import wave
import numpy as np
import pylab as plt

#打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
f = wave.open("noise/sound_Snoise.wav")
#读取格式信息
#一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
#读取波形数据
#读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
str_data  = f.readframes(nframes)
f.close()
#将波形数据转换成数组
#需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
wave_data = np.frombuffer(str_data,dtype = np.int8)
#将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
wave_data.shape = -1,2
#转置数据
wave_data = wave_data.T
#通过取样点数和取样频率计算出每个取样的时间。
time=np.arange(0,nframes)/framerate
print(params)


plt.figure()
# 左声道波形
plt.subplot(2, 1, 1)
plt.plot(time, wave_data[0])
plt.xlabel("时间/s",fontsize=14)
plt.ylabel("幅度",fontsize=14)
plt.title("左声道",fontsize=14)
plt.grid()  # 标尺

plt.show()
