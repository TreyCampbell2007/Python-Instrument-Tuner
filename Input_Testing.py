'''
Input_Testing.py

A file used for testing how to take in the inputs of a microphone on a computer and then 
understand how we could process the microphone input utlizing the fourier transform
'''
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

audioExec = pyaudio.PyAudio()

stream = audioExec.open(format=pyaudio.paFloat32, 
                        channels=1, 
                        rate=44100, 
                        input=True, 
                        frames_per_buffer=1024)

while (True):
    data = stream.read(1024)
    audio = np.frombuffer(data, dtype=np.float32)
    
    # Perform FFT
    spectrum = np.fft.fft(audio)
    frequencies = np.fft.fftfreq(len(audio), 1 / 44100)

    time = np.arange(0, len(audio)) / 44100
    
    # Plot the frequency spectrum
    plt.plot(frequencies, np.abs(spectrum))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.show()

    # Plot the signal
    '''
    plt.plot(time,audio)
    plt.xlabel('Time (s)')
    plt.ylabel('Magnitude')

    plt.show()
    '''
