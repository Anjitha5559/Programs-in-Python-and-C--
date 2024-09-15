# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 08:49:06 2023

@author: anjit
"""
import numpy as np
import matplotlib.pyplot as plt

def RCP(Tsym,alpha,span,L):
    t = np.arange(-span*0.5,(0.5*span)+(1/L),(1/L))
    p = np.zeros(len(t))
    for i in range(len(t)):
        N1 = np.pi * t[i] * (1-alpha) / Tsym
        N2 = np.pi * t[i] * (1+alpha) / Tsym
        N3 = 4 * alpha * t[i] / Tsym
        N4 = np.pi/4 * alpha
        
        Nr = np.sin(N1) + (N3 * np.cos(N2))
        Dr = (np.pi * t[i] /Tsym) *(1- (N3**2))
        if i==(len(t)//2):
            p[i]=(1/np.sqrt(Tsym))*((1-alpha) + (4*alpha)/np.pi)
        elif abs(t[i])==Tsym/(4*alpha):
            p[i]=(alpha/np.sqrt(2*alpha))*(((1+(2/np.pi))*np.sin(N4)) + ((1-(2/np.pi))*np.cos(N4)))
        else:
            p[i]=(1/np.sqrt(Tsym))*(Nr/Dr)
    return p
Tsym = 1
alpha = 0.4
span = 8 * Tsym
L = 16
t = np.arange(-span*0.5,(0.5*span)+(1/L),(1/L))
raised_cosine_pulse = RCP(Tsym, alpha, span, L)
plt.plot(t,raised_cosine_pulse)
no_of_bits = 16
ups = np.zeros(no_of_bits * L)
ups[::L] = np.random.choice([-1,1],no_of_bits)
filtered_output = np.convolve(raised_cosine_pulse, ups)
snr_in_db = 10
snr = 10**(snr_in_db/10)
signal_power = np.sum(ups**2)/len(ups)
N0 = signal_power/snr
noise = np.sqrt(N0/2)*np.random.standard_normal(len(filtered_output))
channel_output = filtered_output + noise
matched_filter_output = np.convolve(channel_output, raised_cosine_pulse)
downsampled = matched_filter_output[span*L:len(matched_filter_output) - span*L]
sampled_output = np.sign(downsampled[::L])
plt.subplot(421)
plt.title("Raised Cosine Pulse")
plt.plot(t,raised_cosine_pulse)
plt.subplot(422)
plt.title("Input")
plt.stem(ups[::L])
plt.subplot(423)
plt.title("Upsampled")
plt.plot(np.arange(len(ups)), ups)
plt.subplot(424)
plt.title("Transmitted Signal")
plt.plot(np.arange(len(filtered_output)),filtered_output)
plt.subplot(425)
plt.title("noise")
plt.plot(np.arange(len(channel_output)),noise)
plt.subplot(426)
plt.title("channel_output")
plt.plot(np.arange(len(channel_output)),channel_output)
plt.subplot(427)
plt.title("matched_filter_output")
plt.plot(np.arange(len(matched_filter_output)),matched_filter_output)
plt.subplot(428)
plt.title("sampled_output")
plt.stem(np.arange(len(sampled_output)),sampled_output)
for i in range(10,No_of_bits-10):
    plt.plot(np.arange(L),matched_filter_output[i*L:((i+1)*L)])
plt.show()