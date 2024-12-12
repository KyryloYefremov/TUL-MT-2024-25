def invert_code_correction(input_numbers: tuple[int, int], debug: bool = False):
    if len(input_numbers) != 2:
        raise ValueError("Input must be 2 numbers as a tuple")

    first, second = input_numbers

    # convert to 8bit bin
    bin_first = format(first, '08b').lstrip('-')
    bin_second = format(second, '08b').lstrip('-')
    if debug:
        print('recieved: ', bin_first, bin_second)

    # check if zeros count in first is odd. If it is => invert the second number
    if bin_first.count('0') % 2 != 0:
        second = abs(second - 255)
        bin_second = format(second, '08b').lstrip('-')

    if debug:
        print('decoded: ', bin_first, bin_second)

    # cacl xor of two numbers
    xor = format(first ^ second, '08b').lstrip('-')
    if debug:
        print(f"xor: {xor}")

    # find the wrong digit index
    if xor.count('0') == 1:
        # error is in information part
        wrong_digit_idx = xor.index('0')
        bin_first_list = list(bin_first)
        bin_first_list[wrong_digit_idx] = "0" if bin_first_list[wrong_digit_idx] == "1" else "1"
        bin_first = ''.join(bin_first_list)

        info = ('1', wrong_digit_idx+1)
    else:
        # error is in the slave part
        wrong_digit_idx = xor.index('1')
        info = ('2', wrong_digit_idx+1)

    return bin_first, info


if __name__ == "__main__":
    data = [160, 223, 64, 65, 128, 126]

    for i in range(1, len(data), 2):
        print('Numbers: ', data[i-1:i+1])
        res = invert_code_correction((data[i-1], data[i]))
        
        bin_num, info = res
        print(f"Output: {int(bin_num, 2)}")
        print(f"Error in number {info[0]}, position: {info[1]}\n")
