# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
#   3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
#   letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
#   letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
#   numbers is in compliance with British usage.
#
# -----
#
# Strategy:
#
# - Break out the commonly used words for numbers, including 'and', and create a map
# - Create some usage rules?
# - Loop through 1 to 1000, and evaluate each number against the rules
#

written_number_map = {
    0: ("", 0),
    1: ("one ", 3),
    2: ("two ", 3),
    3: ("three ", 5),
    4: ("four ", 4),
    5: ("five ", 4),
    6: ("six ", 3),
    7: ("seven ", 5),
    8: ("eight ", 5),
    9: ("nine ", 4),
    10: ("ten ", 3),
    11: ("eleven ", 6),
    12: ("twelve ", 6),
    13: ("thirteen ", 8),
    14: ("fourteen ", 8),
    15: ("fifteen ", 7),
    16: ("sixteen ", 7),
    17: ("seventeen ", 9),
    18: ("eighteen ", 8),
    19: ("nineteen ", 8),
    20: ("twenty ", 6),
    30: ("thirty ", 6),
    40: ("forty ", 5),
    50: ("fifty ", 5),
    60: ("sixty ", 5),
    70: ("seventy ", 7),
    80: ("eighty ", 6),
    90: ("ninety ", 6),
    "00": ("hundred ", 7),
    "000": ("thousand ", 8),
    "and": ("and ", 3)
}

# Test
# number_range = 125

# Real deal
number_range = 1000


def main():
    letter_counter = 0
    for number in range(1, number_range + 1):
        print("------", number, "------")

        num_length = len(str(number))
        answer_key = []
        numword = ""
        if num_length > 3:
            answer_key.extend(thousands_generator(number, num_length))
        if num_length > 2:
            answer_key.extend(hundreds_generator(number, num_length))
        if num_length >= 1:
            answer_key.extend(tens_and_ones_generator(number, num_length))

        tmp_count = 0
        for key in answer_key:
            numword += written_number_map[key][0]
            tmp_count += written_number_map[key][1]
        print(numword, ":", tmp_count)
        letter_counter += tmp_count
    print("==============================================")
    print("answer", letter_counter)


def tens_and_ones_generator(_number, _len):
    _numstr = str(_number)
    _numlist = _numstr[-2:]
    _number_list = []

    if _len > 1:
        if int(_numlist[0]) == 1:
            # Teen
            _number_list.append(int(_numlist))
        else:
            # Not a teen, but tens
            _tensnum = _numlist[0] + "0"
            _number_list.append(int(_tensnum))
            if int(_numlist[-1:]) > 0:
                _number_list.append(int(_numlist[-1:]))

    else:
        _number_list.append(int(_number))

    return _number_list


def hundreds_generator(_number, _len):
    _numstr = str(_number)
    _numlist = _numstr[-3:]
    _number_list = []
    if int(_numlist[0]) > 0:
        _number_list.append(int(_numlist[0]))
        _number_list.append("00")

    if int(_numstr[-2:]) > 0:
        # If there are numbers after the hundreds place, add "and"
        _number_list.append("and")

    return _number_list


def thousands_generator(_number, _len):
    _numstr = str(_number)
    _numlist = _numstr[-4:]
    _number_list = []
    if int(_numlist[0]) > 0:
        _number_list.append(int(_numlist[0]))
        _number_list.append("000")

    return _number_list


if __name__ == "__main__":
    main()
