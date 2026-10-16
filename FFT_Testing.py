'''
FFT_Testing.py

A file utilized for testing my understanding of FFTs and working the with matplotlib extension

This file specifically follows a tutorial from GeeksForGeeks going over the discrete fourier trasform:
https://www.geeksforgeeks.org/data-analysis/discrete-fourier-transform-dft-using-scipy/

'''
import numpy as np
from scipy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

# Choose how many times we sample the signal over the time interval
sampleRate = 1000

# Creates a list of values that are equally spaced from the initial value to the final value
time = np.linspace(0, 1, sampleRate, endpoint=False) 

# The desired frequency that I want to produce
frequency = 30

# Composite signal: Sin
signal =  0.5 * np.sin(2 * np.pi * frequency * time)

# Create noise and add to the signal
noise = 0.5 * np.random.random(sampleRate)
signal = signal + noise

# FFT and inverse FFT
N = len(time)
yf = fft(signal) 
xf = fftfreq(N, 1/(sampleRate)) 

# Gets only the real numbers output from the FFT algorithm
xf = xf[:N//2]
yf = 2.0/N * np.abs(yf[:N//2])

# Visualization
plt.figure(figsize=(10, 4))

# Signal
plt.subplot(1,2,1)
plt.plot(time,signal)
plt.title("Input Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# FFT output utilizing matplotlib
plt.subplot(1,2,2)
plt.xlim(10,50)
plt.plot(xf,yf)
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()