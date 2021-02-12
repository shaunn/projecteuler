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

sum_of_triplet = 1000


def main():
    a = 1
    b = 1
    c = 1

# 1    print(1000**(1/2))
#     exit()
    while True:
        print(a,b,c)

        whilegit stat a >= b:
            b += 1

        while b >= c:
            c += 1


        h = eval_pythagoreanEquation(a, b, c)
        print(h)

        # If eval_pythagoreanEquation returns false
        if not h:
            c = int((a ** 2 + b ** 2)**(1/2))
            a += 1
            # print(eval_pythagoreanEquation(a, b, c)[1])
            # print(c,c ** 2)
            # print("here",h[1])
            # c += 1

        else:
            b += 1
            print("c",c)
            if a + b + c == sum_of_triplet:
                print("yay")
            else:
                print("non")

        if a+b+c == 1000:
            print(a,b,c)
            print("break")
            break

        print("sum",a+b+c)
        if a+b+c < 1000:
            print(a,b,c)
            print("saveme")
            a += 1
            # break
        else:
            break


def eval_pythagoreanEquation(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


if __name__ == "__main__":
    main()
