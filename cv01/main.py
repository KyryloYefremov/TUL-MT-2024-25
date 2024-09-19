import numpy as np
import matplotlib.pyplot as plt
import struct

with open('cv01_dobryden.wav', 'rb') as f:
    # head
    data = f.read(4)
    print(data)
    A1 = struct.unpack('i', f.read(4))[0]  # velikost souboru
    print(A1)

    wafe = f.read(4)
    fmt = f.read(4)
    AF = struct.unpack('i', f.read(4))[0]  # audio format
    K = struct.unpack('h', f.read(2))[0]  # kategorie formatu
    C = struct.unpack('h', f.read(2))[0]    # pocet kanalu

    VF = struct.unpack('i', f.read(4))[0]  # vzorkovaci frekvence
    print(VF)

    PB = struct.unpack('i', f.read(4))[0]  # pocet bytu za sekundu
    VB = struct.unpack('h', f.read(2))[0]  # pocet bytu za vzorek
    VV = struct.unpack('h', f.read(2))[0]  # velikost vzorku
    dta = f.read(4)  # data

    A2 = struct.unpack('i', f.read(4))[0]  # pocet bitu do konce souboru
    print(A2)

    # data
    SIG = np.zeros(A2)
    for i in range(0, A2):
        SIG[i] = struct.unpack('B', f.read(1))[0]
    t = np.arange(A2).astype(float) / VF
    plt.plot(t, SIG)
    plt.xlabel('t[s]')
    plt.ylabel('A[-]')
    plt.show()