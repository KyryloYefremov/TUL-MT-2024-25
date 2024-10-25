import compresser as comp
import numpy as np


if __name__ == "__main__":
    # 1. 
    data_cv06 = np.fromfile('cv06/Cv06_RLE_data.bin', dtype=np.uint8).tolist()
    coded_data = comp.code_RLE(data_cv06)
    decoded_data = comp.decode_RLE(coded_data)
    print("1) RLE compression:")
    print(f"Original data:\n{''.join(map(str, data_cv06))}\n")
    print(f"Coded data:\n{coded_data}\n")
    print(f"Decoded data:\n{''.join(map(str, decoded_data))}")

    print("\n" + "=" * 50, end="\n\n")

    # 2.
    data_cv05 = np.fromfile('cv06/Cv05_LZW_data.bin', dtype=np.uint8).tolist()
    data_str = [str(d) for d in data_cv05]
    coded_data, code_dict = comp.code_huffman(data_str)
    decoded_data = comp.decode_huffman(coded_data, code_dict)

    print("2) Huffman compression:")
    print(f"Original data:\n{''.join(data_str)}\n")
    print(f"Coded data:\n{coded_data}")
    print(f"Code dict:\n{code_dict}\n")
    print(f"Decoded data:\n{''.join(decoded_data)}")