import numpy as np
import matplotlib.pyplot as plt
import struct


def read_wav(filename):
    try:
        with open(filename, 'rb') as f:
            # head
            riff = f.read(4)
            A1 = struct.unpack('i', f.read(4))[0]
            wafe = f.read(4)
            if riff != b'RIFF':
                raise ValueError("Spatny format souboru WAV (RIFF chybi)")
            if wafe != b'WAVE':
                raise ValueError("Spatny format souboru WAV (WAVE chybi)")

            fmt = f.read(4)
            AF = struct.unpack('i', f.read(4))[0]  # audio format
            K = struct.unpack('h', f.read(2))[0]  # kategorie formatu
            C = struct.unpack('h', f.read(2))[0]  # pocet kanalu
            VF = struct.unpack('i', f.read(4))[0]  # vzorkovaci frekvence
            PB = struct.unpack('i', f.read(4))[0]  # pocet bytu za sekundu
            VB = struct.unpack('h', f.read(2))[0]  # pocet bytu za vzorek
            VV = struct.unpack('h', f.read(2))[0]  # velikost vzorku
            VV //= 8

            if K != 1:
                raise ValueError(f"Spatny format souboru WAV (neni PCM)")

            # data
            data_str = f.read(4)
            A2 = struct.unpack('i', f.read(4))[0]

            if VV == 1:
                dtype = 'b'
            elif VV == 2:
                dtype = 'h'
            elif VV == 4:
                dtype = 'i'
            elif VV == 8:
                dtype = 'q'
            else:
                raise ValueError("Neznamy format vzorku")

            # Signal o rozmererch (pocet kanalu x delka vzorku v kanale)
            signal = np.zeros((C, A2 // (C * VV))).astype(float)

            try:
                for sample in range(A2 // VV):
                    sample_channel, sample_num = sample % C, sample // C
                    signal[sample_channel, sample_num] = struct.unpack(dtype, f.read(VV))[0]
            except Exception as e:
                raise ValueError(f"Chyba pri cteni dat: {e}")

            # plot
            time = np.arange(A2 // (C * VV)).astype(float) / VF
            if C == 1:
                plt.plot(time, signal[0])
            if C == 2:
                fig, axs = plt.subplots(C)
                axs[0].plot(time, signal[0])
                axs[1].plot(time, signal[1])
                for ax in axs.flat:
                    ax.set(xlabel='t[s]', ylabel='A[-]')
            if C == 4:
                fig, axs = plt.subplots(2, 2)
                axs[0, 0].plot(time, signal[0])
                axs[0, 1].plot(time, signal[1])
                axs[1, 0].plot(time, signal[2])
                axs[1, 1].plot(time, signal[3])
                for ax in axs.flat:
                    ax.set(xlabel='t[s]', ylabel='A[-]')
            plt.show()

    except Exception as e:
        print(f'\nChyba pri cteni souboru {filename}:')
        print(e)


if __name__ == '__main__':
    files = ['cv02_wav_01.wav',
             'cv02_wav_02.wav',
             'cv02_wav_03.wav',
             'cv02_wav_04.wav',
             'cv02_wav_05.wav',
             'cv02_wav_06.wav',
             'cv02_wav_07.wav', ]
    # files = ['cv02_wav_07.wav']
    for file in files:
        read_wav(file)
