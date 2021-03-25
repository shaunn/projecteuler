
discovered_results = []

# # The test
# test_results = [1634, 8208, 9474]
# power = 4

# The real deal
power = 5

def main():
    # Can't ever be 1
    base = 1200
    # while True:
    while base < 9999999:
        base += 1
        summer = 0
        for i in str(base):
            # print(base, i)
            summer += (int(i)**power)
            # print("summer",summer)

        if base == summer:
            discovered_results.append(base)

    print(discovered_results)
    answer = 0
    for x in discovered_results:
        answer += x

    print("answer",answer)


def get_ceiling(power):
    # Find the limit where the composition of digits to the provided power exceeds the possible number of digits
    # Going the wrong path here

    pass



if __name__ == "__main__":
    main()