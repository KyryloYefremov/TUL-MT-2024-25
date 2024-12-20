import random

from generator import generate_prime_numbers
from coder import *


def main():
    primes = generate_prime_numbers()

    num1, num2 = random.sample(primes, 2)
    print(f"Random prime numbers: \n{num1}, {num2}")

    message = input("Write down message to code :D\n: ")
    ascii_message = [ord(char) for char in message]
    
    coded_message, key = code_RSA(ascii_message, (num1, num2))
    print(f"\n\nCoded: {coded_message}\n Key: {key}")

    decoded_ascii_message = decode_RSA(coded_message, key)
    decoded_message = ''.join([chr(num) for num in decoded_ascii_message])
    print(f"Decoded: {decoded_message}")


if __name__ == "__main__":
    main()