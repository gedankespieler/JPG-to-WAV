import numpy as np
import simpleaudio as sa
import wave
from libjpeg import decode

#uses image.jpg as the source
with open('image.jpg', 'rb') as f:
    arr = decode(f.read())

newarr = []

sounds = [0, 0, 0]
fs = 44100

#create 3 wavs out of the 3 RGB values
for k in range(0, 3):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            newarr.append(arr[i][j][k])
    if len(newarr) % 2 != 0:
        newarr.pop()
    sounds[k] = np.asarray(newarr).tobytes()
    #writes to wav1, wav2, etc.
    ob = wave.open('wav %d.wav' % k, 'wb')
    ob.setnchannels(1)
    ob.setsampwidth(2)
    ob.setframerate(fs)
    ob.writeframesraw(sounds[k])
