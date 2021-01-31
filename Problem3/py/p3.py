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
# primes = [prime_candidate]
# Minimally load the array
# primes = [1, 2, 3]
primes = []

def main():
    print("number: ", number)
    print(3%2)
    # exit()
    quotient_of_prime(number)


def quotient_of_prime(dividend):
    print("----quotient_of_prime--------------------")

    print("dividend ", dividend)
    prime = get_next_prime(prime_candidate)
    factor_test = dividend % prime
    quotient = dividend / prime
    # for loop on known primes?
    # How efficient is that?


def get_next_prime(_prime_candidate):
    print("----get_prime--------------------")
    _unknown_prime = True

    # for testing
    _prime_candidate = 8

    print("initial prime candidate: ", _prime_candidate)



    # exit()

    # Searchimus Prime
    while _unknown_prime:
        # If it is a known prime, lookup and return
        if member_of_known_primes(_prime_candidate):
            #
            return _prime_candidate



        # Determine if the candidate is divisible by a known prime
        for _known_prime in primes:
            if _known_prime != 1:
                print("modulus ", _prime_candidate % _known_prime)
            if _prime_candidate % _known_prime == 0 and _known_prime != 1:
                # The candidate is divisible to a known prime, therefore not a prime.
                print("Not a prime")
                _prime_candidate = _prime_candidate + 1

            continue
            if _prime_candidate < _known_prime:
                print("why am I here")
                # I should have caught the lower primes by now...
                _prime_candidate = _prime_candidate + 1
        else:
            print("maybe prime?")
        # It is not divisible by a known prime, but may be a prime itself
        # Since the number provided may be larger than a known prime determine
        #   every prime until it is equal to or greater than the candidate

        if _prime_candidate > primes[-1]:
            print("last known prime is less")
            _prime_candidate = _prime_candidate + 1




        # primes.append(_prime_candidate)
        # _unknown_prime = False

            print("Potential prime: ", _prime_candidate)

                # Assuming it is for now... TODO





        print("_prime_candidate ++ ", _prime_candidate)

        exit()

                # _unknown_prime = False
                # return _prime_candidate

        # This stops the loop for testing
        if _prime_candidate == 50:
            _unknown_prime = False



    print("amihere?")
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
    # If the known prime list is empty, do some basic population
    # until the modulus returns a 0
    print("im here")
    if not primes:
        # Just load the first three primes
        # primes.extend([1, 2, 3])
        # 0 is not a prime
        # _no_known_primes = True
        _seed = 1
        primes.append(_seed)
        _first_nonprime_found = False
        while not _first_nonprime_found:
            _seed = _seed + 1
            print("New seed: ", _seed)
            if _seed > 10:
                exit()
            if _seed%primes[-1] != 0:
                print(primes[-1])
                print("mod: ",_seed%primes[-1])
                if primes[-1] != 1:
                    # _first_nonprime_found = True
                    print("here")
                    primes.append(_seed)
                    print("Primes: ", primes)

                else:
                    _first_nonprime_found = True
            else:
                primes.append(_seed)
                print("Primes: ", primes)





# print(primes)
#     exit()


        # A prime is divisible by 1 and its self only, so is almost any
        # other number so...Need to confirm that the number isn't
        # divisible by any other primes
        # Sticking to what we know....

        # Iterate until we get a modulus that is not zero?

        # return member_of_known_primes(_candidate)
        # if _candidate%primes[-1] == 0 and _candidate != 1:
        #     seed=seed+1
        #     print("ha")
        #

        #     _seed_candidate = 1
        #     if _seed_candidate/1 == _seed_candidate and _seed_candidate/_seed_candidate == 1:
        # primes.extend(_seed_candidate):
    #     # print("ha")
    #
    # if _candidate not in primes:
    #     return False










    # Determine if the candidate is already a known prime
    # Don't do any more work than you have to
    # if _candidate in primes:
    #     # It has already been determined that it is a prime number
    #     return True
    #
            # return False





def divisible_perfect_power(_dividend, _divisor):
    print("filler")


if __name__ == "__main__":
    main()
