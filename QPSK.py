import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# Initialzing the values
Ac = 1
fc = 10000
L = 32
no_of_bits = 16
fs = L * fc

# Defining the time domain
t = np.arange(0, 1 / fc, 1 / fs)

# Defining the carrier waves
carrier1 = Ac * np.cos(2 * np.pi * fc * t)
carrier2 = -1 * Ac * np.sin(2 * np.pi * fc * t)

# Defining the input data
data = np.random.choice([-1, 1], no_of_bits)

# Seperating out the even and odd indexes
even_indexes = data[::2]
odd_indexes = data[1::2]

# Upsampling the data
even_input = np.zeros(L * no_of_bits // 2)
odd_input = np.zeros(L * no_of_bits // 2)
even_input[::L] = even_indexes
odd_input[::L] = odd_indexes

# Implementing BPSK for both the even and odd parts separately and adding the two signals to obtain the QPSK signal
BPSK_even = np.convolve(even_input, carrier1)
BPSK_odd = np.convolve(odd_input, carrier2)
BPSK_even = BPSK_even[:len(BPSK_even) - L + 1]
BPSK_odd = BPSK_odd[:len(BPSK_odd) - L + 1]
QPSK = BPSK_even + BPSK_odd

# Defining the parameters of the AWGN Channel
SNR_in_dB = 30
SNR_absolute = 10 ** (SNR_in_dB / 10)
signal_power = np.sum(QPSK ** 2)
N0 = signal_power / SNR_absolute
noise = np.sqrt(N0 / 2) * np.random.standard_normal(len(QPSK))
channel_output = QPSK + noise

# The ML demodulator
def demodulator(channel_output, carrier, no_of_bits):
    demodulated_output = np.zeros(no_of_bits)
    for i in range(no_of_bits):
        demodulated_output[i] = np.sign(np.dot(channel_output[i * L:(i + 1) * L], carrier))
    return demodulated_output

# Decoding of the even and odd signals separately by using the two orthonormal carriers
even_out = demodulator(QPSK, carrier1, no_of_bits // 2)
odd_out = demodulator(QPSK, carrier2, no_of_bits // 2)
output = np.zeros(no_of_bits)
output[::2] = even_out
output[1::2] = odd_out

# Plotting the results
plt.subplot(321)
plt.plot(carrier1)
plt.title("Carrier 1")
plt.subplot(322)
plt.plot(carrier2)
plt.title("Carrier 2")
plt.subplot(323)
plt.stem(data)
plt.title("Input Binary Data")
plt.subplot(324)
plt.plot(QPSK)
plt.title("QPSK Signal")
plt.subplot(325)
plt.plot(channel_output)
plt.title("Channel Output")
plt.subplot(326)
plt.stem(output)
plt.title("Decoded Binary Data")
plt.show()

# Evaluating the Bit Error Rates for various SNR
SNR_dB_Array = np.arange(-50, 50, 5)
SNR_Absolute_Array = 10 ** (SNR_dB_Array / 10)
N0_array = signal_power / SNR_Absolute_Array

BER_Array = np.zeros(len(SNR_dB_Array))

for i in range(len(SNR_dB_Array)):
    noiseBER = np.sqrt(N0_array[i] / 2) * np.random.standard_normal(len(QPSK))
    channel_output = QPSK + noiseBER
    demodulated_output_even = demodulator(channel_output, carrier1, no_of_bits // 2)
    demodulated_output_odd = demodulator(channel_output, carrier2, no_of_bits // 2)
    BER_Array[i] = np.round(
        np.sum(even_indexes != demodulated_output_even) / (no_of_bits) + np.sum(odd_indexes != demodulated_output_odd)
    ) / (no_of_bits)

Ideal_BER = 0.5 * scipy.special.erfc(np.sqrt(10 ** (SNR_dB_Array / 10)))

# Plotting the results
plt.semilogy(SNR_dB_Array, BER_Array, label="Simulated Values")
plt.semilogy(SNR_dB_Array, Ideal_BER, label="Theoretical Values")
plt.xlabel("SNR in dB")
plt.ylabel("Probability of Error")
plt.title("Theoretical vs Simulated Bit Error Rate")
plt.legend()
plt.show()
