"""
This module is for testing compresser.py.
It reads Cv05_LZW_data.bin file and apply compression and decompression.
"""

import numpy as np

from compresser import compress_LZW, decompress_LZW


INPUT_FILE = 'cv05/Cv05_LZW_data.bin'


if __name__ == "__main__":
    data = np.fromfile(INPUT_FILE, dtype=np.uint8)
    data_len = data.size

    data_str = ''.join(str(n) for n in data.tolist())
    print(f"\nOriginal data:     {data_str}")

    dictionary = [
        '1', '2', '3', '4', '5',
    ]

    compressed_data = compress_LZW(input_text=data_str, phrases_dict=dictionary)
    com_data_len = len(compressed_data)
    print(f"Compressed data:   {compressed_data}")

    decompressed_data = decompress_LZW(input_numbers=compressed_data, phrases_dict=dictionary)
    print(f"Decompressed data: {decompressed_data}")

    print(f"\nOriginal data == decompressed data: {data_str == decompressed_data}")
    print(f"Original data len: {data_len}, compressed data len: {com_data_len}\n")


