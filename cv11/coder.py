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


def code_move_to_front(input_str: str):
    input_str = input_str.lower()
    stack = [chr(char) for char in range(ord('a'), ord('z')+1)]
    coded_chars = []

    try:
        for char in input_str:
            # get char index
            char_idx = stack.index(char)
            # add its index as new code for this char
            coded_chars.append(char_idx)
            # put this char to the beginning of the stack
            stack.insert(0, stack.pop(char_idx))

        return coded_chars
    except ValueError:
        print("This coding method can code only english chars.")
        raise ValueError


def decode_move_to_front(coded_str: list[int]):
    stack = [chr(char) for char in range(ord('a'), ord('z')+1)]
    decoded_chars = []

    for char_idx in coded_str:
        # add decoded char to result list
        decoded_chars.append(stack[char_idx])
        # put this char to the beginning of the stack
        stack.insert(0, stack.pop(char_idx))
    
    return ''.join(decoded_chars)
