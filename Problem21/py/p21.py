# Let d(n) be defined as the sum of proper divisors of n (numbers less
#   than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
#   pair and each of a and b are called
#   amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
#   44, 55 and 110; therefore d(220) = 284.
#   The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
# ---
#
# Strategy
#
# - Find other divisible factor problems I have solved in the past
# - Create the d(n) function
# - Iterate through n to identify d(n) for all numbers under 1000 and plug into dict
# - Iterate through the d(n) dict and find values that match another d(n) key
#


# Starting prime
prime_prime_candidate = 1

# List of discovered primes
primes = []

# List of discovered d(n) solutions
factor_sums = {}

# List of discovered amicable numbers
amicable_numbers = []

# Tests
# limit = 500

# Real deal
limit = 10000


def main():
    # Prime the primes
    max_potential_factor = int(limit ** (1 / 2))
    prime_factor_generator(max_potential_factor)

    # Iterate through n determining its factors, skipping 0 and 1
    for n in range(2, limit):
        factors = factor_list(n)
        factor_sums[n] = sum(factors)

    # Iterate through the factor_sum values looking for a matching key
    #   indicating an amicable pair
    sum_values = factor_sums.values()
    for sum_value in sum_values:
        amicable_numbers.extend(amicable_list_generator(sum_value))
    print("Sum of amicable numbers:", sum(amicable_numbers))


def amicable_list_generator(_number):
    _return_list = []
    # If the value is a key, but not the same key that produced the value
    if _number in factor_sums and _number != factor_sums[_number] and _number not in amicable_numbers:
        # Key match! Now check for a pair
        if factor_sums[_number] in factor_sums:
            if factor_sums[factor_sums[_number]] == _number:
                _return_list = [factor_sums[_number], factor_sums[factor_sums[_number]]]

    return _return_list


def factor_list(_number):
    _factors = []
    # Iterate primes
    for _prime in primes:
        # Identify prime factors
        if _number % _prime == 0 and _number != _prime:
            _factors.append(_prime)
            # The quotient of the number divided by _prime is also a factor
            _factors.append(int(_number / (_prime)))
        # Identify non-prime factors
        for _multiplier in range(2, _prime + 1):
            while _multiplier < int(_number ** (1 / 2)):
                if _number % _multiplier == 0 and _multiplier not in _factors:
                    _factors.append(_multiplier)
                    # The quotient of the number divided by _multiplier * _prime is also a factor
                    _factors.append(int(_number / _multiplier))
                _multiplier = _multiplier ** 2

    # 1 is always a factor so apply now. According to the rules, the
    #   number itself is not used
    _factors += [1]

    return sorted(set(_factors))


def prime_factor_generator(_max):
    # Initial load of primes array
    if not primes:
        # 1 is NOT a prime. 0 is not either. 2 is the first. TIL
        _prime_candidate = 2
        primes.append(_prime_candidate)
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
    return primes


if __name__ == "__main__":
    main()
