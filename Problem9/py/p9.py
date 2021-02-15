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
        print(a, b, c)
        while a < b:
            c = get_hypotenuse(a, b)
            print(c)
            print(c%1)
            if (c).is_integer():
                print("a:", a)
                print("a:", a, "b:", b, "c:", c)
                print("a+b+c:", a + b + c)
                print("abc", a * b * c)
                # exit()
            else:
                a += 1
            b += 1
        # a = 1
            print("grok",a + b + c )
            print("h:",a + b + c < sum_of_triplets)


# def main():
#     a = b = c = 0
#     while a + b + c < sum_of_triplets:
#         a, b, c = platonic_sequence(a)
#         print(a, b, c)
#         print("a+b+c:", a + b + c)
#
#         if a < b < c and a + b + c == sum_of_triplets:
#             if eval_pythagoreanEquation(a, b, c):
#                 print("a:", a)
#                 print("a:", a, "b:", b, "c:", c)
#                 print("a+b+c:", a + b + c)
#                 print("abc", a * b * c)
#                 exit()
#
#         a += 1

# print("wew lad, that didn't work. Going Euclid")
#
# m = 2
# n = 1
# a = b = c = 0
#
# while a + b + c < sum_of_triplets:
#     a, b, c = euclids_variant(m,n)
#     print(m,n)
#     print(a,b,c)
#     while m > n > 0:
#         n +=1
#     m+=1


def euclids_variant(_m, _n):
    # a=mn,  b=(m^2 - n^2)/2, c=(m^2 + n^2)/2
    # m > n > 0
    _a = int(_m * _n)
    _b = int((_m ** 2 - _n ** 2) / 2)
    _c = int((_m ** 2 + _n ** 2) / 2)
    return _a, _b, _c


def platonic_sequence(_a):
    _b = _c = 0
    # Check if even or odd, then use the appropriate formulae
    if _a % 2 == 1:
        _b = (_a ** 2 - 1) / 2
        _c = (_a ** 2 + 1) / 2
    elif _a % 2 == 0:
        _b = (_a / 2) ** 2 - 1
        _c = (_a / 2) ** 2 + 1
    else:
        # Shouldn't be possible
        exit(1)

    return _a, _b, _c


def get_hypotenuse(_a, _b, _c=False):
    # For validation purposes only
    if _c:
        print("here")
        if _a ** 2 + _b ** 2 == _c ** 2:
            return True
    _c = (_a ** 2 + _b ** 2) ** (1 / 2)
    print(_a, _b, _c)

    return _c


# def pythagoreanEquation(_a, _b, _c = None):
#     if _c is None:
#         _c = (_a ** 2 + _b ** 2)**(1/2)
#     print(_a,_b,_c)
#     if _a ** 2 + _b ** 2 == _c ** 2:
#         return _a, _b, _c
#     return False


if __name__ == "__main__":
    main()
