def num2bin8bit(num: int) -> str:
    bin_num = bin(num)[2:]
    if len(bin_num) >= 9:
        raise ValueError('Can only convert number from 0 to 255, because target binary number must be 8 bits.')
    bin_num_8bit = '0' * (8 - len(bin_num)) + bin_num
    return bin_num_8bit
    

def bin_to_gray_converter(bin_num: str) -> str:
    gray_code_num = list(bin_num)
    try:
        num_start_idx = bin_num.index('1')  # find the first digit '1' appearence in the number
    except:
        # if there is no '1' in the number => it is number zero
        return ''.join(gray_code_num)

    # start with the next index from <num_start_idx> to save the first digit without changes
    for digit_idx in range(num_start_idx+1, len(bin_num)):
        if bin_num[digit_idx-1] == '1':
            digit = str(int(not int(bin_num[digit_idx])))  # invert bin digit
            gray_code_num[digit_idx] = digit

    return ''.join(gray_code_num)
