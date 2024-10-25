import numpy as np
from collections import Counter, defaultdict


def code_RLE(data: list) -> list[tuple[int, int]]:
    # Init
    coded_data = list()
    current_len = 1

    # Per element in data:
    # If two neighbor elements are the same, increase len. Else write element symbol and its len to output.
    try:
        for i in range(len(data)):
            if data[i] == data[i+1]:
                current_len += 1
            else:
                coded_data.append((current_len, data[i]))
                current_len = 1  
    # Raised if we are on the last list element and trying to get the next - means the end of coding
    except IndexError:
        coded_data.append((current_len, data[-1]))


    return coded_data


def decode_RLE(coded_data: list[tuple[int, int]]) -> list[int]:
    decoded_data = list()
    # Per combination of element end its len: unpack and write to output
    for length, symbol in coded_data:
        decoded_data += [symbol] * length
    
    return decoded_data    


def code_huffman(data: list[str]) -> tuple[list, dict[str]: str]:
    # Init structures
    counter = Counter(data)
    frequency = counter.most_common()

    coded_symbols = defaultdict(str)

    # While at least two words exists
    while len(frequency) >= 2:
        # Pop two last elements with 2 lowest frequencies
        last_elem, last_freq = frequency.pop()
        prelast_elem, prelast_freq = frequency.pop()

        # For every symbol in elements add current code number:
        for symbol in last_elem:
            coded_symbols[symbol] += '0'  # 0 - for lower frequency
        for symbol in prelast_elem:
            coded_symbols[symbol] += '1'  # 1 - for higher frequency

        # Union 2 elements and add to main list for next processing
        new_elem_frequency = last_freq + prelast_freq
        new_elem = prelast_elem + last_elem
        frequency.append(
            (new_elem, new_elem_frequency)
        )
        
        # Sort list by elements frequency (from max to min)
        frequency = sorted(frequency, key=lambda x: x[1], reverse=True)

    # Revert codes for every symbol ('110' -> '011')
    coded_symbols = {symbol: code[::-1] for symbol, code in coded_symbols.items()}
    # print(coded_symbols)

    # Code the data
    coded_data = []
    for symbol in data:
        coded_data.append(coded_symbols[symbol])
        
    return coded_data, coded_symbols


def decode_huffman(coded_data: list, coded_symbols: dict) -> list:
    decoded_data = []
    # Extract symbols and their zero-one codes to separate lists
    symbols, codes = list(coded_symbols.keys()), list(coded_symbols.values())

    # Per symbol of coded data
    for coded_symbol in coded_data:
        idx = codes.index(coded_symbol)
        decoded_data.append(symbols[idx])

    return decoded_data


if __name__ == "__main__":
    """
    Simple testing. Examples from the presentation.
    """

    # 1.
    data = "AAAAAFFFFCHHH"
    coded_data = code_RLE(data)
    decoded_data = decode_RLE(coded_data)
    print(data)
    print(coded_data)
    print(''.join(decoded_data))

    print("-" * 50)

    # 2.
    data_str = 'ABRAKADABRA'
    coded_data, code_dict = code_huffman(data_str)
    decoded_data = decode_huffman(coded_data, code_dict)
    print(data_str)
    print(coded_data)
    print(code_dict)
    print(''.join(decoded_data))



