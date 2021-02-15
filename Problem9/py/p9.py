# The test
# For (3,4,5) representing (a,b,c)
# For (3,4,5) a + b + c = 12 is true
# a < b < c is true for (3,4,5)
# a2 + b2 = c2 is true for (3,4,5)
# For (3,4,5) a + b + c = 12

# Ultimately, find the product abc.

# - Iterate through (a,b) until a^2 + b^2 = c^2
# - Test if a < b < c
# - Test if a + b + c = 1000

# (3,4,5)  3^2 + 4^2 = 5^2    9 + 16 = 25
# (6,8,10) 6^2 + 8^2 = 10^2  36 + 64 = 100

# Tst
# sum_of_triplets = 12

sum_of_triplets = 1000


def main():
    # Starting points for a < b < c
    a = 1
    b = 2
    c = 3

    while a + b + c < sum_of_triplets:
        while a < b:
            c = get_hypotenuse(a, b)
            if (c).is_integer():
                c = int(c)
                if a + b + c > 1000:
                    print("a:", a)
                    print("a:", a, "b:", b, "c:", c)
                    print("a+b+c:", a + b + c)
                    print("abc", a * b * c)
                    exit()
            else:
                a += 1
            b += 1


def get_hypotenuse(_a, _b, _c=False):
    # For validation purposes only
    if _c:
        if _a ** 2 + _b ** 2 == _c ** 2:
            return True
    _c = (_a ** 2 + _b ** 2) ** (1 / 2)
    return _c


if __name__ == "__main__":
    main()
