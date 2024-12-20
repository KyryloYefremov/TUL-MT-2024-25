import string


def caesar_cipher_decrypt(ciphertext, shift):
    alphabet = string.ascii_lowercase
    decrypted_text = []
    
    for char in ciphertext:
        if char in alphabet:
            # shift character by the given amount
            index = (alphabet.index(char) - shift) % 26
            decrypted_text.append(alphabet[index])
        else:
            # non-alphabet characters save without changes
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)


def brute_force_decrypt(ciphertext, keywords):
    # try all 26 shifts
    for shift in range(26): 
        decrypted_text = caesar_cipher_decrypt(ciphertext.lower(), shift)
        if any(keyword in decrypted_text for keyword in keywords):
            return decrypted_text, shift
    return None, None


if __name__ == "__main__":
    keywords = ["roads", "domov"]
    filenames = ['cv14/cv14_text01.txt', 'cv14/cv14_text02.txt']

    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            txt = file.read()
            result = brute_force_decrypt(txt[::-1], keywords)
            print('\n', filename)
            print(f"TEXT: {result[0]}\nSHIFT: {result[1]}")
