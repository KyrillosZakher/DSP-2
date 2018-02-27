
from tkinter import *
from tkinter import ttk
import pyaudio
import numpy as np

root =Tk()


DurationText=Entry(root)
FrequenyText=Entry(root)
PlayButton= Button(root,text="play")


DurationText.pack()
FrequenyText.pack()
PlayButton.pack()


def play():
    p = pyaudio.PyAudio()
    volume = .5  # range [0.0, 1.0]
    fs = 44100  # sampling rate, Hz, must be integer : number op points in one second
    duration = float(DurationText.get())  # input  # in seconds, may be float
    f = float(FrequenyText.get())  # input   # sine frequency, Hz, may be float
    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)
    stream.stop_stream()
    stream.close()



PlayButton.config(command = play)

root.mainloop()
