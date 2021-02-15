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
    a = 1
    # while a + b + c < sum_of_triplets:
    while True:
        # Find primitive triplet for 'a' using Platonic sequence
        a, b, c = platonic_sequence(a)

        # Init a multiplier to loop through in case the answer is not primitive
        k = 0

        # Continuously loop to evaluate primitive multiplied by coefficient
        while (k * (a + b + c)) < sum_of_triplets:
            k += 1
            if k * (a + b + c) == sum_of_triplets and a < b < c:
                # A solution has been found; inform the world
                print("Primitive Triplet: ", a, b, c)
                a = k * a
                b = k * b
                c = k * c
                print("Primitive Multiplier:", k)
                print("Solution Triplet: ", a,b,c)
                print("a + b + c:", a + b + c)
                print("a * b * c:", a * b * c)
                exit()

        # Increment 'a' before being processed at the start of the loop
        a += 1

def platonic_sequence(_a):
    _b = _c = 0
    # Check if even or odd, then use the appropriate formulae
    if _a % 2 == 1:
        _b = (_a ** 2 - 1) / 2
        _c = (_a ** 2 + 1) / 2
    elif _a % 2 == 0:
        _b = (_a / 2) ** 2 - 1
        _c = (_a / 2) ** 2 + 1
    return int(_a), int(_b), int(_c)


if __name__ == "__main__":
    main()
