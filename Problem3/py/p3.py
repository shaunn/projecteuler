# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# The test
# Answer is [5,7,13,29]
number = 13195

# The real deal
# number = 600851475143

# Starting prime
prime_candidate = 1

# List of discovered primes
primes = [prime_candidate]


def main():
    print("number: ", number)
    quotient_of_prime(number)


def quotient_of_prime(dividend):
    print("----quotient_of_prime--------------------")

    print("dividend ", dividend)
    prime = get_next_prime(prime_candidate)
    factor_test = dividend % prime
    quotient = dividend / prime


def get_next_prime(_prime_candidate):
    print("----get_prime--------------------")

    # for testing
    _prime_candidate = 8

    print("initial prime candidate: ", _prime_candidate)

    # If it is a known prime, lookup and return
    if member_of_known_primes(_prime_candidate):
        return _prime_candidate

    # If it is not known, determine
    _unknown_prime = True

    # A prime is divisible by 1 and its self only, so is almost any
    # other number so...Need to confirm that the number isn't
    # divisible by any other primes
    # Sticking to what we know....

    while _unknown_prime:

        # Determine if the candidate is divisible by a known prime
        for _prime in primes:
            if _prime_candidate % _prime == 0:
                # The candidate is divisible to a known prime, therefore not a prime.

                # Increment so we can move along to find the next prime
                _prime_candidate = _prime_candidate + 1
            else:
                # It is not divisible by a known prime, but may be a prime itself
                # Assuming it is for now...


    # Determine if the candidate is divisible by a known prime
    for _prime in primes:
        print("prime ", _prime)
        print("prime_candidate: ", _prime_candidate)
        print("quotient: ", _prime_candidate / _prime)
        while _prime_candidate % _prime == 0:
            # This just tells me it is divisible by a prime
            # ... maybe I should be returning the quotient
            # with this function... its doing too much?
            if _prime_candidate / _prime == 1:
                # Then it's a prime!

                print("am I prime? ", _prime_candidate)
            else:

                _prime_candidate = _prime_candidate + 1

            primes.append(_prime_candidate)
            return _prime_candidate

    print(_prime_candidate)
    exit()


def member_of_known_primes(_candidate):
    # Determine if the candidate is already a known prime
    # Don't do any more work than you have to
    if _candidate in primes:
        # It has already been determined that it is a prime number
        return True


def divisible_perfect_power(_dividend, _divisor):
    print("filler")


if __name__ == "__main__":
    main()
