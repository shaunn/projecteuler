# -*- coding: utf-8 -*-

# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the
#  product of two 3-digit numbers.

# Strategy
# - Take the max of two, three digit numbers, and
# work backwards to find the first palindrome.
#
# Rules:
# - The products must be 3 digits each

# max number that is the product of two three digit
# numbers

# max three digit number
max_factor = 999

# min factor, based on the candidate rules
min_factor = max_factor % 10 ** (len(str(max_factor)) - 1) + 1

# max product possible
max_product = max_factor ** 2

# # Starting prime
# prime_candidate = 1

# List of discovered primes
primes = []

# List of discovered prime factors
prime_factors = []


def main():
    candidate = max_product
    while True:
        palindrome = find_next_palindrome(candidate)

        palindrome_factors = find_factors(palindrome, max_factor, min_factor)
        if palindrome_factors is False:
            candidate = palindrome - 1
        else:
            # Palindrome and rule abiding factors found
            print("palindrome: ", palindrome)
            print("palindrome_factors: ", palindrome_factors)
            break


def find_next_palindrome(_candidate):
    while True:
        # Break the numbers out into an array for analysis
        breakout = list(map(int, str(_candidate)))

        # Identify the number of elements to be compared
        split_length = len(str(_candidate))//2

        # Identify the first and last set; invert the last
        fore = breakout[:split_length]
        aft = breakout[::-1][:split_length]

        if fore == aft:
            # We found a palindrome! Now let's return it
            return _candidate

        # No match; next one down
        _candidate -= 1


def find_factors(_dividend, _divisor, _lower_limit):
    # Rule: Find the largest palindrome made from the
    #  product of two 3-digit numbers.

    # Setting the upper limit to the first provided divisor since
    #   the divisor will only get smaller
    _upper_limit = _divisor
    while True:

        if _dividend % _divisor == 0:
            # Factor has been found! Now to test...

            cofactor = int(_dividend / _divisor)
            # Test that the cofactor does not exceed the upper limit
            if cofactor < _upper_limit:
                # We are good to go! Return
                return _divisor, cofactor
        # Test if lower limit has been reached
        if _divisor <= _lower_limit:
            # No further factors to find
            return False

        # Decrement and rerun
        _divisor -= 1


if __name__ == "__main__":
    main()
