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

sum_of_triplet = 12


def main():
    a = 1
    b = 1
    c = 1

    print(1000**(1/2))
    exit()
    while True:
        if a >= b:
            b += 1

        if b >= c:
            c += 1

        h = eval_pythagoreanEquation(a, b, c)
        print(h)

        # If eval_pythagoreanEquation returns false
        if not h[0]:

            print(eval_pythagoreanEquation(a, b, c)[1])
            print(c,c ** 2)
            print("here",h[1])
            c += 1

        else:
            print("c",c)

        if a+b+c >= 1000:
            print(a,b,c)
            print("saveme")
            break


def eval_pythagoreanEquation(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False, a ** 2 + b ** 2


if __name__ == "__main__":
    main()
