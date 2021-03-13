# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
# Strategy
#
# Brute force this sucker
# ref: https://projecteuler.net/problem=48

# Test
# limit = 10

# Real deal
limit = 1000


def main():
    summer = 0
    for num in range(1, limit + 1):
        summer += (num ** num)

    print(num, summer)
    print("answer:", str(summer)[-10:])


if __name__ == "__main__":
    main()
