import numpy as np
import matplotlib.pyplot as plt
import scipy.special

Ac = 1
fc = 10000
L = 32
fs = L * fc

No_of_bits = 512

t = np.arange(0, 1 / fc, 1 / fs)

carrier = Ac * np.cos(2 * np.pi * fc * t)

input = np.zeros(len(t) * No_of_bits)

input[::L] = np.random.choice([1, -1], No_of_bits)

BPSK = np.convolve(carrier, input)
BPSK = BPSK[:len(BPSK) - L + 1]

SNR_in_dB = 10
SNR = 10 ** (SNR_in_dB / 10)
signal_power = np.sum(BPSK ** 2) / No_of_bits
N0 = signal_power / SNR

noise = np.sqrt(N0 / 2) * np.random.standard_normal(len(BPSK))

channel_output = BPSK + noise

def demodulator(channel_output, carrier, no_of_bits):
    demodulated_output = np.zeros(no_of_bits)
    for i in range(no_of_bits):
        demodulated_output[i] = np.sign(np.dot(channel_output[i * L:(i + 1) * L], carrier))
    return demodulated_output

demodulated_output = demodulator(channel_output, carrier, No_of_bits)

plt.subplot(321)
plt.title("Carrier Wave")
plt.plot(carrier)
plt.subplot(322)
plt.title("Input Data")
plt.stem(input[::L])
plt.subplot(323)
plt.title("BPSK Signal")
plt.plot(BPSK)
plt.subplot(324)
plt.title("Noise Signal Signal")
plt.plot(noise)
plt.subplot(325)
plt.title("AWGN Channel output")
plt.plot(channel_output)
plt.subplot(326)
plt.title("Decoded Output")
plt.stem(demodulated_output)
plt.show()

SNR_dB_Array = np.arange(-20, 10, 1)
SNR_Array = 10 ** (SNR_dB_Array / 10)
N0_Array = signal_power / SNR_Array
BER = np.zeros(len(SNR_Array))

for i in range(len(SNR_Array)):
    received_signal = BPSK + ((np.sqrt(N0_Array[i] / 2))) * np.random.standard_normal(len(BPSK))
    demodulated_output = demodulator(received_signal, carrier, No_of_bits)
    BER[i] = np.sum(input[::L] != demodulated_output) / No_of_bits

Ideal = 0.5 * scipy.special.erfc(np.sqrt(10 ** (SNR_dB_Array / 10)))

plt.semilogy(SNR_dB_Array, Ideal)
plt.xlabel('SNR in dB')
plt.ylabel('Bit Error Rate')
plt.semilogy(SNR_dB_Array, BER)
plt.title('Theoretical vs Simulated Bit Error Rate')
plt.legend(['Theoretical', 'Simulated'])
plt.show()
