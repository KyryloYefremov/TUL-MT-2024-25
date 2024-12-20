from generator import generate_prime_numbers


def code_RSA(message: list[int], primes: tuple[int, int]) -> tuple[list[int], tuple[int, int]]:
    """
    Code the given msg using RSA algorithm.
    Returns:
        tuple contains:
        - list of coded symbols (list of integers)
        - tuple that contains 2 keys: public and private key
    """
    num1, num2 = primes

    module = num1 * num2  # module, public
    
    # use Euler function to calculate upper number of interval, from where should be taken encrypting exponent
    ef = (num1 - 1) * (num2 - 1)

    primes = generate_prime_numbers((2, ef))
    decrypt_key = None
    i = 0
    # find the decryption key `d` as mod(exp * d) = Ef  - congruence of residual classes
    # try different `encypt_exp`
    while not decrypt_key:
        encrypt_exp = primes[i]
        for n in range(2, ef):
            if (encrypt_exp * n) % ef == 1:
                decrypt_key = n
                break
        i += 1  # try with next `encrypt_exp`

    # print(ef)
    # print(encrypt_exp)
    
    coded_message = []
    for number in message:
        coded_message.append(pow(number, encrypt_exp, module))

    return coded_message, (decrypt_key, module)


def decode_RSA(coded_message: list[int], key: tuple[int, int]) -> list[int]:
    decrypt_key, module = key

    decoded_message = list()
    for number in coded_message:
        decoded_message.append(pow(number, decrypt_key, module))
    
    return decoded_message
