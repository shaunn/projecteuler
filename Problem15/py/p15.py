# Starting in the top left corner of a 2×2 grid, and only being able
#   to move to the right and down, there are exactly 6 routes to the
#   bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#
# ----
#
# Strategy
#
# - Looked this up; using combination formula
# - n!/(k!(n-k)!)
# - where n is the number of squares to traverse
# - k is the number or directions that can be taken per square


# Test
# x_max = 2
# y_max = 2

# # Real deal
x_max = 20
y_max = 20


def main():
    # number_steps_to_finish
    n = x_max + y_max
    # number_of_moves_in_one_direction
    k = 20  # right or down

    combination_of_different_paths = int(factorial(n) / (factorial(k) * factorial(n - k)))
    print(combination_of_different_paths)


def factorial(_x):
    _factorial = 1
    while _x >= 0:
        for i in range(1, _x + 1):
            _factorial *= i
        return _factorial
    # Don't care to handle negatives


if __name__ == "__main__":
    main()
