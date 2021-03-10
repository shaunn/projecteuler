# Using names.txt (right click and 'Save Link/Target As...'), a 46K text
#   file containing over five-thousand first names, begin by sorting it
#       into alphabetical order. Then working out the alphabetical value
#       for each name, multiply this value by its alphabetical position
#       in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
#   is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
#   COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
#
# ----
#
# Strategy
#
# - Load names.txt
# - Sort names in alphabetical order. The order is important? TBD if Colin is 938th
# - Establish an alphabetical value map
# - Loop through each name
# - Map the value of each value of the name into a list, then sum
# - Add up all the names
#
# The Test
#
# - When the list is sorted into alphabetical order, COLIN, which is
#   worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#   So, COLIN would obtain a score of 938 × 53 = 49714.
#
# Mucking around:
#
# - print(names_list.index('COLIN')) returns 937, not 938
#


alphabetical_numeric_value = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


def main():
    f = open("../p022_names.txt", "r")
    names_raw = f.read()
    names_raw_no_quote = names_raw.replace('"', '')
    names_list = names_raw_no_quote.split(",", )
    names_list.sort()

    summer = 0
    for name in names_list:
        name_index = names_list.index(name)
        name_sum = 0
        for letter in name:
            name_sum += alphabetical_numeric_value[letter]

        summer += name_sum * (name_index + 1)

    print("Total of all the name scores in the file:", summer)


if __name__ == "__main__":
    main()
