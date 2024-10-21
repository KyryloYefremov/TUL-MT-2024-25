"""
This module contains 2 functions to compress and decompress data using Lempel-Ziv-Welch algorithm.
"""

def compress_LZW(input_text: str, phrases_dict: list[str]) -> list[int]:
    phrases_dict = phrases_dict.copy()

    # Init variables
    output = []
    index = -1
    is_input_end = False

    # While not the end of the input text
    while not is_input_end:
        found_phrase = ''
        found_new_phrase = False
        
        # While new phrase isn't found
        while not found_new_phrase:
            try:
                # New phrase = previous phrase + input symbol
                found_phrase = found_phrase + input_text[index + 1]
                # If a phrase is in phrases dicionary, get its index
                if found_phrase in phrases_dict:
                    index += 1
                    current_output = phrases_dict.index(found_phrase) + 1
                # Else add new phrase to phrases dicionary and keep on search for new phrases
                else:
                    phrases_dict.append(found_phrase)
                    found_new_phrase = True
            # Is raised when we are trying to get symbol from input that doesn't exist (is higher than input size).
            # Stop finding new phrases, save output and return
            except IndexError:
                is_input_end = True
                found_new_phrase = True

        output.append(current_output)

    return output.copy()


def decompress_LZW(input_numbers: list[int], phrases_dict: list[str]) -> str:
    phrases_dict = phrases_dict.copy()

    # Init variables
    output = []
    output_phrase = ''

    # Per number of sequence
    for index in range(len(input_numbers)):

        try:
            # Save previous output
            prev_phrase = output_phrase
            # Convert number back to phrase
            phrase_num = input_numbers[index]
            output_phrase = phrases_dict[phrase_num - 1]
            # Build new phrase as: previous output + first symbol of current output
            new_phrase = prev_phrase + output_phrase[0]
        # Raised if current input number is not in phrases dictionary (a number > than phrases_dict list)
        except IndexError:
            # Output: previous phrase + first symbol of previous phrase
            output_phrase = prev_phrase + prev_phrase[0]
            new_phrase = output_phrase
            
        output.append(output_phrase)
        if new_phrase not in phrases_dict:
            phrases_dict.append(new_phrase)

    return ''.join(output)



if __name__ == "__main__":
    """
    Simple testing (example from the lecture).
    """
    
    inp = 'abcabcabcbcba'
    dic = ['a', 'b', 'c']
    
    res = compress_LZW(inp, dic)
    print(res)

    dec_res = decompress_LZW(res, dic)
    print(dec_res)

    print(inp == dec_res)

