# 2520 is the smallest number that can be divided by each of the
#   numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible
#   by all of the numbers from 1 to 20?
#
# ----
# Strategy:
# - Identify the highest divisor (20) as the candidate
# - Via loop, test the candididate modulus against a decrementing
#       set of divisors
# - First fail, increment the candidate by 20

high_divisor = 20


def main():
    # Got to start somewhere...
    candidate = high_divisor
    while True:
        # Array to track divisors
        divisors = []

        for _divisor in range(high_divisor, 0, -1):
            # Check the modulus between the candidate and the divisor
            if candidate % _divisor == 0:
                divisors.append(_divisor)
            else:
                # Increment the candidate and break out of the loop
                candidate += high_divisor
                continue

        if len(divisors) == high_divisor:
            # If we are here, we must have a winner!
            break

    print("the smallest positive number that is evenly divisible ")
    print(" by all of the numbers from 1 to", high_divisor, "is", candidate)


if __name__ == "__main__":
    main()
