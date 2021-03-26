factor_map = {0: {'factorial': 1, 'length': 1}}
answer_list = []

# Test
limit = 9999999


def main():
    # print(factorialish(10, 12))
    build_factor_map()
    print(factor_map)
    for number in range(1,limit + 1):
        # print(number)
        summer = 0
        for digit in str(number):
            if factor_map[int(digit)]['length'] > len(str(number)):
                break
            else:
                summer += factor_map[int(digit)]['factorial']
        if summer == number:
            answer_list.append(number)

    print(answer_list)
    result = 0
    for answer in answer_list:
        result += answer


    print("Result:", result - 3)

def build_factor_map():
    for i in range(1, 10):
        _fact = i
        for j in range(1, i):
            _fact = _fact * j
        factor_map[i] = {'factorial': _fact, 'length': len(str(_fact))}


if __name__ == "__main__":
    main()

# def factorialish(_base, _limit):
#     for i in range(_base, 0, -1):
#         _base = _base * i
#         print(i, _base)
#
#         if _base > limit:
#             return False
#     return _base
