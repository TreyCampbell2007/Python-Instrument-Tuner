'''
TunerSimulator.py

Focusing on creating simulated signals close to what would occur in a microphone when playing 
an instrument. Then perform DSP algorithms to see what errors would occurs.

'''

# To make an accurate simulation of a microphone input, I want to make the signal change over time
# This would make it similar to real input.
import numpy as np
from scipy.fft import fft, ifft, fftfreq
import matplotlib.pyplot as plt

# Base variables
frequency = 220 # A3 note
fs = 44100 # sample rate

time = np.arange(0, 1.0, 1/fs) # 1 second of time values

signal = 0.5 * np.sin(2 * np.pi * frequency * time) # Creates an array of signal values for that time

# Create harmonics for the instruments
signal = (signal 
          + 0.3 * np.sin(2 * np.pi * 2 * frequency * time) # 440 Hz
          + 0.2 * np.sin(2 * np.pi * 0.5 * frequency * time) # 110 Hz
          + 0.15 * np.sin(2 * np.pi * 0.25 * frequency * time) # 65 Hz
          + 0.2 * np.sin(2 * np.pi * 3 * frequency * time)) # 660 Hz

# Create noise for the instrument
noise = 0.05 * np.random.randn(len(time))
signal = signal + noise

# Now we want to go through the signal and process each individual window

window_size = 4096

frame = signal[0:window_size]
jump = 1024
num = 0

for start in range(0, len(signal) - window_size, jump):
    frame = signal[start:start + window_size]
    # Now we can analyze that individual frame

    print(frame.argmax())