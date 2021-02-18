# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def main():
    # s is starting, n are the terms in the chain
    s = n = 0

    chain_len_list = []
    while True:
        s += 1
        # s = 837798
        n = s

        chain_list = [s]
        # print("----------")
        if s == 1000000:
            print("The starting number that produces the "
                  "longest chain:", chain_len_list.index(max(chain_len_list))+1)
            print("max",max(chain_len_list))
            break

        while n != 1:
            # print("s",s)
            #
            # print("n",n)
            #
            # print("n % 2",n % 2)
            # print("1 % 2",1 % 2)
            if n % 2 == 0:
                n = int(n/2)
                # print("even")
            else:
                n = 3*n + 1
                # print("odd")

        # print("n",n)
            chain_list.append(n)
        # print("s",s,"len(chain_list)",len(chain_list))
        chain_len_list.append(len(chain_list))
        # print("chain_len_list",chain_len_list)
        # print("chain_list",chain_list)
        # print("s",s)
        # print("chain_len_list.index(max(chain_len_list))",chain_len_list.index(max(chain_len_list))+1)
        # break





if __name__ == "__main__":
    main()