import math


def generate_prime_numbers(interval: tuple[int, int] = (1000, 10000)):
    start, end = interval

    # if the interval is invalid
    if start > end:
        start, end = end, start

    # create an array for the range [2, sqrt(end)]
    sqrt_end = int(math.sqrt(end)) + 1
    is_prime_small = [True] * (sqrt_end + 1)
    is_prime_small[0] = is_prime_small[1] = False  # 0 and 1 are not primes

    # find small primes
    for i in range(2, int(math.sqrt(sqrt_end)) + 1):
        if is_prime_small[i]:
            for multiple in range(i * i, sqrt_end + 1, i):
                is_prime_small[multiple] = False

    small_primes = [i for i, is_prime in enumerate(is_prime_small) if is_prime]

    # use the small primes to mark non-primes in the [start, end] range
    range_size = end - start + 1
    is_prime_range = [True] * range_size

    for prime in small_primes:
        # find the first multiple of `prime` in the range [start, end]
        first_multiple = max(prime * prime, (start + prime - 1) // prime * prime)

        # mark all multiples of `prime` as non-prime
        for multiple in range(first_multiple, end + 1, prime):
            is_prime_range[multiple - start] = False

    # extract primes from the range
    primes = [num for num, is_prime in zip(range(start, end + 1), is_prime_range) if is_prime]

    return primes


if __name__ == "__main__":
    primes = generate_prime_numbers((10, 25))
    print(primes)