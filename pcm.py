import numpy as np
import matplotlib.pyplot as plt

fm = 100
tm = 1 / fm
fs = 50 * fm
ts = tm / 500
B = 1
t = np.arange(0, tm, ts)
x = B + np.sin(2 * np.pi * fm * t)
SNR = []
n_bits = []  # New array to store the number of bits per symbol

for n in range(4, 20, 1):
    l = 2 ** n
    print(l)
    step = (max(x) - min(x)) / l
    q = step * np.floor(x / step)
    q1 = q + step / 2
    plt.plot(t, q1)
    for i in range(0, len(x)):
        s = int(q[i] / step)
        binary_representation = bin(s)[2:].zfill(n)
        print(binary_representation)
    error = x - q
    print(error)
    power = (x @ x) / len(x)
    power_noise = (error @ error) / len(x)
    snr = 10 * np.log10(power / power_noise)
    print(snr)
    SNR.append(snr)
    n_bits.append(n)  # Append the number of bits (n) to the n_bits array

# Plotting the SNR versus number of bits per symbol
plt.figure()
plt.plot(n_bits, SNR, 'o-')
plt.title('SNR vs Number of Bits per Symbol')
plt.xlabel('Number of Bits per Symbol (n)')
plt.ylabel('SNR in dB')
plt.grid(True)
plt.show()
