import librosa
audio_file = 'Recording.wav'
x, sr = librosa.load(audio_file)

from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import librosa.display

X = librosa.stft(x) # computing the STFT
Xdb = librosa.amplitude_to_db(abs(X)) # convert amplitide to dB scale
plt.figure(figsize=(14,5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()