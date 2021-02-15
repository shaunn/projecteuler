# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# The test
# number = 10
# Answer is 17

# The real deal
number = 2000000

# List of discovered primes
primes = []

# List of discovered prime factors
prime_factors = []


def main():
    nth_prime = prime_factor_generator(number)
    print("The last prime below", number, "is", nth_prime[-1])
    print(primes)
    print(sum(primes))


def prime_factor_generator(_max):
    # Initial load of primes array
    if not primes:
        # 1 is NOT a prime. 0 is not. 2 is the first. TIL
        _prime_candidate = 2
        primes.append(_prime_candidate)
        # print("New prime:",_prime_candidate)
    # "prime" the primes array! Get it?
    _prime_candidate = primes[-1]
    if _prime_candidate in primes:
        _prime_candidate = primes[-1] + 1

    while True:
        for _prime in primes:
            if _prime_candidate % _prime == 0:
                _prime_candidate += 1
                break
        else:
            if _prime_candidate > _max:
                break
            else:
                primes.append(_prime_candidate)
                # print("New prime:",_prime_candidate)
    return primes


if __name__ == "__main__":
    main()
