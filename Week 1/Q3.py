import librosa
audio_file = 'Original.wav'
x, sr = librosa.load(audio_file)
print(x.shape, sr)
librosa.output.write_wav('Slower1.wav', x, int(sr/2))
librosa.output.write_wav('Faster1.wav', x, sr*2)