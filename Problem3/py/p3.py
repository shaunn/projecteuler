# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# The test
# number = 13195
# Answer is [5,7,13,29]

# The real deal
number = 600851475143

# Starting prime
prime_prime_candidate = 1

# List of discovered primes
primes = []

# List of discovered prime factors
prime_factors = []


def main():
    print("Find the largest prime factor of ", number)
    prime_factor_search(number)
    print("Answer: ", prime_factors[-1])


def prime_factor_search(_dividend):
    # Initial load of primes array
    if not primes:
        # 1 is a prime. 0 is not
        primes.append(1)
        # "prime" the primes array! Get it?
    _prime_candidate = primes[-1]
    if _prime_candidate in primes:
        _prime_candidate = primes[-1] + 1

    while True:

        if _prime_candidate > _dividend:
            break

        for _prime in primes:
            if _prime == 1:
                continue
            if _prime_candidate % _prime == 0:
                _prime_candidate += 1
                break
        else:
            primes.append(_prime_candidate)
            if _dividend % primes[-1] == 0:
                # Add this new prime to the prime_factors array
                prime_factors.append(primes[-1])
                _dividend = _dividend / primes[-1]
                print("New _dividend", _dividend)
                _prime_candidate += 1


if __name__ == "__main__":
    main()
