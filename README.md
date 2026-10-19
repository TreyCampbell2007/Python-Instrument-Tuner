# Python-Instrument-Tuner
### Project Goals
Take a microphone input from the user utilizing PyAudio, which will then run through a Digital Signal Processing (DSP) algorithm that processes the frequency and returns that musical note that is being produced along with how many cents off the note is from being in tune. The program should be able to run in real time and process signals consistently, with accuracy.

### Personal Goals
- Get familiar with the use of fourier transforms for processing signal data
- Get comfortable with the use of scipy/numpy for signal processing
- Understand the basic concepts and concerns when creating DSP algorithms
- Keep good documentation such that others can learn from reading this project

## Prerequisite Knowledge
### Tuner Algorithm
So, how does a tuner actually work? In general, we know a tuner wants to take in a piece of audio and then, depending on the frequency of the signal, display what note it is hearing and how close the input audio is to being in tune with the note closest to it. So, for example, the note A is generally tuned to 440 Hz. So, if our tuner were to take in the input of 447 Hz, we would display them playing an A, but then showcase they are not 'in tune' with the exact frequency and are instead a certain amount of 'cents' away from the frequency, in which cents are the form of measurement for how out of tune you are from a notes frequency.

But here's the challenge, the input audio signal isn't just a single frequency, it is a mixture of the many different incoming audio signals that are being produced when the tuner is on. So, we have to take this array of audio and know which signal to pick out and also make sure that we're only picking up signals when they pass a certain threshold of volume. We only worry about notes above a certain threshold because we want to ignore the natural noise frequencies that are coming into the microphone. 

But there's one more challenge, how does our code actually figure out what notes (frequencies) are being input into the microphone? The microphone takes in a audio signal that is a mixture of the other signals, not just one signal. So what we want to do is take this mixture of signals, and split it up into an array of the individual signals that make up the input audio. How do you do this? Using the fourier transform.

### The Fourier Transform
The Fourier Transform is a mathematical operation that takes the input signal and turns it into an array of the different signals that make up the original signal. Now, for the sake of this project I won't be going into the math that allows us to do this (also because I haven't yet taken the class that has taught me this), but I will go into how exactly we will use this.

Now it is important to keep in mind that the fourier transform that is being used in code is actually the **Fast Fourier Transform** (FFT), which is a discrete version of the fourier transform built for coding purposes. The inputs that we take into the computer aren't continuous, but rather a set of discrete 1s and 0s that represent the input signal. So, the fourier transforms we use will actually be performing use the FFT algorithm.

So, I think the best way to showcase the FFT is by showcasing the graphs that are produced from an example fourier transform on a simple 10 Hz signal, showcased below:

<img width="999" height="398" alt="Screenshot 2026-10-16 181653" src="https://github.com/user-attachments/assets/8a29164e-a133-487e-a6cf-5bee81612dba" />

In the above example, we have a signal of 10 Hz displayed on the left, and the product of the fourier transform graphed on the right, where we can see that the only signal it detects being the 10Hz. Hopefully, this is where it kind of clicks how a tuner is possible to create. Since we can imagine a graph on the right that has a bunch of signals of varying amplitudes of which we can choose which signal to process depending on their amplitudes. 

Here's an example of a 30 Hz signal with some added noise could look like and what the FFT could produce:

<img width="999" height="401" alt="Screenshot 2026-10-16 185319" src="https://github.com/user-attachments/assets/c24b4963-2698-43b3-8921-fdee5a83e43e" />

## Simulation
To start off this project, I want to do two things:
- Simulate signals similar to what the microphone would input, such as simulating specific frequencies and noise (Partially done above for example, but want to test more to improve accuracy to real microphone inputs).
- Test DSP algorithms on these simulated signals to understand problems that could occur when processing actual signals

The simulation for this will be done on the TunerSimulator.py file in the testing folder.


