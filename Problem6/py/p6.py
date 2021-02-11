# The sum of the squares of the first ten natural numbers is:
#
# 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
#
# (1^2 + 2^2 + 3^2 + ... + 10^2) = 55^2 = 3025
#
#
# Hence the difference between the sum of the squares of the
#   first ten natural numbers and the square of the sum is:
# 3025 - 385 = 2640
#
#
# Find the difference between the sum of the squares of the
#   first one hundred natural numbers and the square of the sum.
#
# ----
#
# Strategy:
# - Loop from 1 through 100, squaring each
# - Get the sum of all of the squares
# - square the sum
#

# Define the max number of natural numbers to be processed
natural_max = 100


def main():
    # Declare the variables important to developing solution
    sum_of_naturals = 0
    sum_of_squares = 0

    for _natural_number in range(1, natural_max + 1):
        sum_of_naturals += _natural_number
        sum_of_squares += _natural_number ** 2
    square_of_sum = sum_of_naturals ** 2
    diff = square_of_sum - sum_of_squares

    print("Difference between the sum of the squares of the")
    print(" first one hundred natural numbers and the square")
    print(" of the sum of the first",natural_max,"natural numbers: ",diff)


if __name__ == "__main__":
    main()
