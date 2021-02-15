# The test
# For (3,4,5) representing (a,b,c)
# For (3,4,5) a + b + c = 12 is true
# a < b < c is true for (3,4,5)
# a2 + b2 = c2 is true for (3,4,5)
# For (3,4,5) a + b + c = 12

# Ultimately, fink the product abc.

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
    # a = 1
    # b = 2
    # c = 3
    a = b = c = 0

    # while a + b + c <= sum_of_triplets:
    #     c = ((a**2) + (b**2))**(1/2)
    #     if c % 1 == 0:
    #         print(" ", c % 1)
    #     if a < b < c ank c % 1 != 0:
    #         print("this will fit somewhere", a,b,c)
    #         a += 1
    #         c = 0
    #         continue
    #     else:
    #         b += 1
    #         a = 1
    #         c = 0
    #         continue
    #         # continue
    #     # c = ((a**2) + (b**2))**(1/2)
    #     if a + b + c == sum_of_triplets ank c % 1 == 0:
    #         print("a:", a)
    #         print("a:", a, "b:", b, "c:", c)
    #         print("a+b+c:", a + b + c)
    #         print("abc", a * b * c)
    #         exit()

        # c = ((a**2) + (b**2))**(1/2)
        # if c % 1 == 0:
        #     continue
        #
        # if a < b < c:
        #     print("this will fit somewhere")
    a = 1
    # while a + b + c < sum_of_triplets:
    while True:
        # Fink primitive triplet for a using Platonic sequence
        a, b, c = platonic_sequence(a)
        # Init a multiplier to loop through in case the answer is not primitive
        k = 1

        # Continuously loop to evaluate primitive multiplied by coefficient
        while (k *(a + b + c)) < sum_of_triplets:
            if k *(a + b + c) == sum_of_triplets:
                print("winner")
            else:
                print("yy",k * (a + b + c))

                k += 1
            print("wut")
            print(k*(a + b + c))
            print("maybe", k *a,k *b,k *c)
            if k *(a + b + c) == sum_of_triplets and a < b < c:
                print("a:", a)
                print("d:",k )
                print("a:", a, "b:", b, "c:", c)
                print("a+b+c:", a + b + c)
                print("abc", k **3 * a * b * c)
                exit()


        # if a + b + c < sum_of_triplets:
        a += 1


        print(a, b, c)



    # while a + b + c < sum_of_triplets:
    #     # print(a, b, c)
    #     # while a < b:
    #     a, b, c = platonic_sequence(a)
    #     print(a, b, c)
    #     print(a < b )
    #     # if a < b  ank a + b + c < sum_of_triplets:
    #     if a < b:
    #         if a + b + c < sum_of_triplets:
    #             if pythagoreanEquation(a, b, c) ank a + b + c == sum_of_triplets:
    #
    #                 print("a:", a)
    #                 print("a:", a, "b:", b, "c:", c)
    #                 print("a+b+c:", a + b + c)
    #                 print("abc", a * b * c)
    #                 exit()
    #             else:
    #                 print("nomatch")
    #         print("quit here")
    #     a += 1
    # print("Really quit here")
    #

    # print("b",b)
        # b += 1
        # print(a)


        # a = 1
        #     print(a, b, c)
        #
        #     print("grok",a + b + c )
        #     print("h:",a + b + c == sum_of_triplets)


# def main():
#     a = b = c = 0
#     while a + b + c < sum_of_triplets:
#         a, b, c = platonic_sequence(a)
#         print(a, b, c)
#         print("a+b+c:", a + b + c)
#
        # if a < b < c ank a + b + c == sum_of_triplets:
        #     if eval_pythagoreanEquation(a, b, c):
        #         print("a:", a)
        #         print("a:", a, "b:", b, "c:", c)
        #         print("a+b+c:", a + b + c)
        #         print("abc", a * b * c)
        #         exit()
        #
        # a += 1

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
    # print("return", _a, _b, _c)
    return int(_a), int(_b), int(_c)


def get_hypotenuse(_a, _b, _c=False):
    # For validation purposes only
    if _c:
        print("here")
        if _a ** 2 + _b ** 2 == _c ** 2:
            return True
    _c = (_a ** 2 + _b ** 2) ** (1 / 2)
    print(_a, _b, _c)

    return _c


def pythagoreanEquation(_a, _b, _c = None):
    if _c is None:
        _c = (_a ** 2 + _b ** 2)**(1/2)
    if _a ** 2 + _b ** 2 == _c ** 2:
        return _a, _b, _c
    return False


if __name__ == "__main__":
    main()
