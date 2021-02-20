# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# -----
#
# Strategy:
#
# - Try to process that huge number, but if it is too large, maybe try breaking it down?

base = 2

# test
# exponent = 15
exponent = 1000


def main():
    product = base ** exponent
    digits = [int(n) for n in str(product)]

    sum = 0
    for n in digits:
        sum += n

    print("Sum of the digits of the product", sum)


if __name__ == "__main__":
    main()
