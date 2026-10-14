'''
FFT_Testing.py

A file utilized for testing my understanding of FFTs and working the with matplotlib extension

This file specifically follows a tutorial from GeeksForGeeks going over the discrete fourier trasform:
https://www.geeksforgeeks.org/data-analysis/discrete-fourier-transform-dft-using-scipy/

'''
import numpy as np
from scipy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

# Create a time vector
sampleRate = 1000

# Creates a list of values that are equally from the initial value to the final value
time = np.linspace(0, 1, sampleRate, endpoint=False) 

# Composite signal: sine + cosine
signal =  0.5 * np.sin(2 * np.pi * 120 * time) + 5 * np.cos(2 * np.pi * 20 * time) + np.sin(2*np.pi*time)

# FFT and inverse FFT
N = len(time)
yf = fft(signal)
xf = fftfreq(N, 1/sampleRate)

# Need to look into why they do this to xf and yf?
xf = xf[:N//2]
yf = 2.0/N * np.abs(yf[:N//2])

print(max(yf))

# Visualization
plt.figure(figsize=(10, 4))

# FFT output utilizing matplotlib
plt.subplot(1, 1, 1)
plt.plot(xf,yf)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()