

# Test
number = 5


# Real Deal
# number = 100

result_list = []

def main():
    for a in range(1, number + 1):
        for b in range(1, number + 1):
            result_list.append(a**b)

    # answer = list(set(result_list))
    answer = list(set(result_list))
    print("list", result_list)
    print("answer list:", answer)
    print("answer", len(answer))

def repeat_remover(_list):


if __name__ == "__main__":
    main()