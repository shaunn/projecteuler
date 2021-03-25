

# Test
# number = 5


# Real Deal
number = 100

result_list = []

def main():
    for a in range(2, number + 1):
        for b in range(2, number + 1):
            result_list.append(a**b)

    # answer = list(set(result_list))
    answer = repeat_remover(result_list)
    print("answer: ", sorted(answer))
    print("answer: ", len(answer))

def repeat_remover(_list):
    _return_list=[]
    print("list",_list)
    _set = list(set(_list))
    print("set",_set)
    return sorted(_set)
    # for n in _set:
    #     print("n",n)
    #     # print(_list.count(n))
    #     if _list.count(n) == 1:
    #         _return_list.append(n)

    return _return_list

if __name__ == "__main__":
    main()