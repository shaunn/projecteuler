# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# ----
# Strategy
#
# - Dust off my old prime code from problem 3
# - Iterate through primes until I have 10,001 of them

# Not very creative tonight with this variable
n = 10001

primes = []


def main():
    nth_prime = prime_factor_generator(n)
    print("The last prime out of a list of", n, "is", nth_prime)


def prime_factor_generator(_limit):
    # Initial load of primes array
    if not primes:
        # 1 is a prime. 0 is not
        primes.append(1)
        # "prime" the primes array! Get it?
    _prime_candidate = primes[-1]
    if _prime_candidate in primes:
        _prime_candidate = primes[-1] + 1

    while True:

        if len(primes) > _limit:
            return primes[-1]

        for _prime in primes:
            if _prime == 1:
                continue
            if _prime_candidate % _prime == 0:
                _prime_candidate += 1
                break
        else:
            primes.append(_prime_candidate)


if __name__ == "__main__":
    main()
