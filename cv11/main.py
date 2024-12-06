from coder import *


def task01(nums_to_convert: int):
    """
    TASK 01:
    Naprogramujte převodník mezi binárním a Grayovým kódem pro 8 bitů. Výsledek čísel 0 až 255 vypište do konzole.
    """
    print("TASK 01 (GRAY CODE)")
    nums = range(nums_to_convert)
    print(f"NUM      BIN      GRAY")
    for num in nums:
        bin_num = num2bin8bit(num)
        gray_num = bin_to_gray_converter(bin_num)
        print(f"{num:03}:  {bin_num}  {gray_num}")
        

def task02():
    """
    TASK 02:
    Naprogramujte Move-To-Front algoritmus (filtr) - kodér i
    dekodér. Výstup z kodéru i dekodéru vypište do konzole.
    Vstup bude řetězec písmen (A až Z - bez diakritiky) napsaný
    na klávesnicí a odeslaný pomocí klávesy ENTER.
    """
    print("TASK 02 (MTV)")
    is_valid = False
    while not is_valid:
        try:
            input_str = input("Type string: ")
            coded_input = code_move_to_front(input_str)
            decoded_input = decode_move_to_front(coded_input)
            is_valid = True
        except ValueError:
            print('Try one more time!\n')

    print(f"INPUT STRING:   {input_str}")
    print(f"CODED STRING:   {coded_input}")
    print(f"DECODED STRING: {decoded_input}\n")
    


def task03():
    """
    Naprogramujte Burrows-Wheelerovu Transformaci - kodér i
    dekodér. Výstup z kodéru i dekodéru vypište do konzole.
    Vstup bude řetězec písmen (A až Z - bez diakritiky) napsaný
    na klávesnicí a odeslaný pomocí klávesy ENTER.
    """
    print("TASK 03 (BWT)")
    input_str = input("Type string: ")
    coded_input, input_str_index = code_burrows_wheeler(input_str)
    decoded_input = decode_burrows_wheeler(coded_input, input_str_index)

    print(f"INPUT STRING:   {input_str}")
    print(f"CODED STRING:   {coded_input}, index: {input_str_index}")
    print(f"DECODED STRING: {decoded_input}\n")


if __name__ == "__main__":
    task01(nums_to_convert=8)
    print('\n\n')
    task02()
    print('\n\n')
    task03()