from coder import *


def task01():
    """
    TASK 01:
    Naprogramujte převodník mezi binárním a Grayovým kódem pro 8 bitů. Výsledek čísel 0 až 255 vypište do konzole.
    """
    nums = range(256)
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
    ...

if __name__ == "__main__":
    # task01()
    task02()