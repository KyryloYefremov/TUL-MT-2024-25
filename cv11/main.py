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
    ...


def task03():
    """
    Naprogramujte Burrows-Wheelerovu Transformaci - kodér i
    dekodér. Výstup z kodéru i dekodéru vypište do konzole.
    Vstup bude řetězec písmen (A až Z - bez diakritiky) napsaný
    na klávesnicí a odeslaný pomocí klávesy ENTER.
    """
    ...

if __name__ == "__main__":
    task01()