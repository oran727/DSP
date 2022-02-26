import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

b1 = signal.firwin(40, 0.2)
b2 = signal.firwin(41, [0.3, 0.8])
b3 = signal.firwin(3, 0.1, window='boxcar',pass_zero='highpass')
w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)
w3, h3 = signal.freqz(b3)


plt.title('Digital filter frequency response')

plt.plot(w3, 20*np.log10(np.abs(h3)), 'g')
plt.ylabel('Amplitude Response (dB)')
plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()