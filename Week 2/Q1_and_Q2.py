import numpy
import librosa
sr = 22050 # sample rate
T = 5.0 # duration of signal
t = numpy.linspace(0, T, int(T*sr), endpoint = False) # creates an array of timestamps
x1 = 0.5*numpy.sin(2*numpy.pi*256*t)
x2 = 0.5*numpy.sin(2*numpy.pi*256*2*t)
x3 = 0.5*numpy.sin(2*numpy.pi*256*3*t)
x4 = 0.5*numpy.sin(2*numpy.pi*256*4*t)
x=x1+x2+x3+x4
librosa.output.write_wav('Resultant.wav', x, sr)

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt # this package is used for making graphs
import librosa.display

plt.figure(figsize=(14,5))
plt.plot(x1[1000:1100])
plt.grid()

plt.figure(figsize=(14,5))
plt.plot(x2[1000:1100])
plt.grid()

plt.figure(figsize=(14,5))
plt.plot(x3[1000:1100])
plt.grid()

plt.figure(figsize=(14,5))
plt.plot(x4[1000:1100])
plt.grid()

plt.figure(figsize=(14,5))
plt.plot(x[1000:1100])
plt.grid()

X1 = librosa.stft(x1) # computing the STFT
Xdb1 = librosa.amplitude_to_db(abs(X1)) # convert amplitide to dB scale
plt.figure(figsize=(14,5))
librosa.display.specshow(Xdb1, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()

X = librosa.stft(x) # computing the STFT
Xdb = librosa.amplitude_to_db(abs(X)) # convert amplitide to dB scale
plt.figure(figsize=(14,5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()