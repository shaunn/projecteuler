# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
#
# ```
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
# ```
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?
#
# ------
#
# Strategy
#
# - Create a matrix and load values into a list of lists
# - Traverse each element in the row
# - Create a temp list comprising of a legal set of elements that existing extending out in eight directions
# - If the set is "illegal" i.e. the range goes beyond the boundaries of the grid, set phantom elements to zero or skip
# - Compute the product of all elements in this tmp list and store it in a results list
# - Find the max value in the results list and return it
#

adjacent_range = 4

input_grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

product_store = []


def main():
    # Create the matrix
    matrix = load_grid(input_grid)

    # Using a,b instead of x,y because it will be confusing
    #   without normalizing so it isn't y,x
    # a = 0  # Vertical, or row index
    # b = 0  # Horizontal, or column index

    a_max = len(matrix[0])
    b_max = len(matrix)

    for a in range(a_max):
        for b in range(b_max):
            process_adjacent_products(matrix, (a, b), adjacent_range)

    print("Greatest product of four adjacent numbers in the same direction:")
    print(max(product_store))


def process_adjacent_products(_matrix, _coordinates, _range):
    # Moving counter-clockwise: E, SE, S, SW, W, NW, N, NE
    # But I think just going NE, E, SE, and S will cover it, all other
    #   directions being redundant since starting at 0,0

    products_right_to_left(_matrix, _coordinates, _range)
    products_diagonal(_matrix, _coordinates, _range)
    products_top_down(_matrix, _coordinates, _range)

    # A rerun of products_diagonal with the matrix flipped
    _matrix.reverse()
    products_diagonal(_matrix, _coordinates, _range)


def products_right_to_left(_matrix, _coordinates, _range):
    # The easiest method
    _a = _coordinates[0]
    _b = _coordinates[1]
    _tmp_list = []

    # So easy
    _tmp_list = _matrix[_a][_b:_b + _range]

    # Get the product and store it
    product_store.append(get_product_of_list(_tmp_list))


def products_diagonal(_matrix, _coordinates, _range):
    # A bit tricky, but manageable
    _a = _coordinates[0]
    _b = _coordinates[1]
    _tmp_list = []

    for _step in range(_range):
        # This test is to avoid index out of range errors
        if _a + _step < len(_matrix[0]) and _b + _step < len(_matrix):
            # Increment both a and b by one
            _tmp_list.append(_matrix[_a + _step][_b + _step])

    # Get the product and store it
    product_store.append(get_product_of_list(_tmp_list))


def products_top_down(_matrix, _coordinates, _range):
    _a = _coordinates[0]
    _b = _coordinates[1]
    _tmp_list = []

    if _a + _range >= len(_matrix):
        _range = len(_matrix) - _a + 1
    for _step in range(_range):
        if _a + _step >= len(_matrix):
            continue
        _tmp_list.append(_matrix[_a + _step][_b])

    product_store.append(get_product_of_list(_tmp_list))


def get_product_of_list(_list):
    _product = 1
    for _factor in _list:
        _product *= _factor
    return _product


def load_grid(_input):
    _output_matrix = []
    _tmp_table = list(map(str, _input.split("\n")))
    for _tmp_row in _tmp_table:
        _elements = list(map(int, _tmp_row.split(" ")))
        _output_matrix.append(_elements)

    return _output_matrix


if __name__ == "__main__":
    main()
