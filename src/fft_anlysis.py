import numpy as np
import pandas as pd
from scipy.signal import coherence, csd
from scipy.fft import fft, fftfreq

def compute_returns(prices):
    return np.log(prices).diff().dropna()

def compute_fft(signal, sampling_rate = 1.0 ):
    n = len(signal)
    yf = fft(signal.values)
    xf = fftfreq(n, 1 / sampling_rate)[n // 2:]
    magnitude = 2.0 / n*np.abs(yf[n // 2:])
    return xf, magnitude

def compute_coherence(signal1, signal2, fs=1.0, nperseg=256):
    f, Cxy = coherence(signal1, signal2, fs=fs, nperseg=nperseg)
    return f, Cxy

def compute_cross_spectrum(signal1, signal2, fs=1.0, nperseg=256):
    f, Pxy = csd(signal1, signal2, fs=fs, nperseg=nperseg)
    phase = np.angle(Pxy)
    delay = np.zeros_like(phase)
    nonzero = f != 0
    delay[nonzero] = phase[nonzero] / (2 * np.pi * f[nonzero])
    return f, np.abs(Pxy), phase, delay