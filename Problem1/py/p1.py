# divisors of 3 and 5
#
# Problem 1
# If we list all the natural numbers below 10 that are divisors of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these divisors is 23.
#
# Find the sum of all the divisors of 3 or 5 below 1000.

# Strategies
#
# 1. `remainder = dividend - divisor * quotient` and `remainder=0`
# 2. Using the built-in modulo function
# 3. Using the built-in remainder function

# Packages! tbd...

# Constants and variables!
# Set the upper limit
upper_limit = 1000

# Set the list of divisors to test against
divisors = [3, 5]

# Define the 'summer' containing the running of sums
summer = 0


# Functions!
def test_if_multiple(test_number, test_divisor):
    if test_number < test_divisor:
        return False
    if test_zero_using_modulo_function(test_number, test_divisor):
        return True
    else:
        return False

def test_zero_using_modulo_function(test_number, test_divisor):
    # 2. Using the built-in modulo function
    test = test_number % test_divisor
    if test == 0:
        return True
    else:
        return False

def main():
    global summer
    # Note that the range function is the total number of elements starting at 0.
    # Conveniently this satisfies the "below 1000" requirement out of the box!
    for number in range(upper_limit):
        # Rules state 'Find the sum of all the divisors of 3 or 5'
        # Once a match is found for the multiple, don't perform further processing
        multiple = False
        for divisor in divisors:
            if not multiple:
                if test_if_multiple(number, divisor):
                    multiple = True
                    summer = summer + number

    print(str(summer))



if __name__ == "__main__":
    main()
