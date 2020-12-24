#coding : utf-8

import numpy as np
from glob import glob
import time, sys
import wave
import matplotlib.pyplot as plt

wav = wave.open("Files/ciermx.wav","r")

raw = wav.readframes(-1)

raw = np.frombuffer(raw,"Int16")

sampleRate = wav.getframerate()

if wav.getnchannels() == 2 :
    print("stereo files are not supported. Use  mono files")
    sys.exit(0)

time = np.linspace(0, len(raw)/sampleRate, num = len(raw))

plt.title("waveForm of Wave File")
plt.plot(time,raw,color="red")
plt.ylabel("Amplitude")
plt.show()