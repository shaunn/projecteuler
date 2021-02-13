# The four adjacent digits in the 1000-digit number that
#   have the greatest product are 9 × 9 × 8 × 9 = 5832.
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit
#   number that have the greatest product. What is the
#   value of this product?
#
# ----
#
# Strategy
#
# _ Break the number into an array
# - Grab first 4/13 elements, calculate their product,
#    stash in an array/map/hash/whatevs
# - shift one number over, do what I did above
# - If there is a zero in the 4/13 set, shift just
#    beyond and repeat evaluation
# - When there are no four-digit groups to evaluate,
# - Sort the stash hash, find the greatest product, and
#    pump it out



# A list of the products of the subsets
subset_products = []

super_number_block = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""


def main():
    # Convert the super number string to an actual
    #   number. Watch me convert it to a string and
    #   then an array later
    super_number = int(super_number_block.replace("\n", ""))

    # Told you
    super_array = list(map(int, str(super_number)))
    # Define the length of a sliding list of adjacent values
    # adjacent_range = 4
    adjacent_range = 13

    while True:
        candidate_subset = []

        for x in range(0, adjacent_range):
            # print(super_array[x])
            candidate_subset.append(super_array[x])

        if 0 in super_array[0:adjacent_range]:
            # print("of course", super_array[0:adjacent_range])
            skip_index = find_last_zero(super_array[0:adjacent_range])
            super_array = super_array[skip_index:]
        else:
            # Find the product of the first array
            subset_product = array_product(candidate_subset)

            # Append the newly discovered subset_product to the subset_products list
            subset_products.append(subset_product)
            # Chop off the first subset from the super_array
            super_array = super_array[adjacent_range:]

        # If the remaining number of elements is less than 1, break out. If greater
        #   than one but less than the adjacent_range window, readjust the window
        #   and process the subset anyways
        if len(super_array) < 1:
            # We're done here
            break
        elif len(super_array) < adjacent_range:
            # print("len(super_array",len(super_array))
            # print("adjacent_range", adjacent_range)
            adjacent_range = len(super_array)

    print("Highest product of",adjacent_range,"adjacent digits is",max(subset_products))

def find_last_zero(_array):
    # test
    # _array = [0,1,0,1]
    # _array = [0,1,1,1]
    _array = [2,1,0,0]
    # print("_array",_array)
    # Confirm there is a zero. I don't trust the other guy
    if 0 in _array:
        #  index() function only returns the first occurrence, so reverse the list
        #   since there could be multiple zeros and process from there
        _array.reverse()
        _last_zero_index_reverse = _array.index(0)

        _last_zero_index = (len(_array) - 1) - _last_zero_index_reverse
        # print("_last_zero_index", _last_zero_index)
        return _last_zero_index

def array_product(_input_array):
    # Needs to be one because this is a multiplying function
    result = 1
    for element in _input_array:
        result = element * result

    return result


if __name__ == "__main__":
    main()
