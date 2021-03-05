# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# -----
#
# Strategy
#
# - Do what the man said; Find the sum of the digits in the number 100!
#
#
#

# Test
# base = 10

# Real deal
base = 100


def main():
    x = 1
    for m in range(1, base + 1):
        x = x * m

    number_string = str(x)
    summer = 0
    for c in number_string:
        summer += int(c)

    print(base,"! produces the sum",summer)

if __name__ == "__main__":
    main()
