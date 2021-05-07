# Solution to Problem 0014

# COLLATZ

def collatz_iteration(n):
    
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def solution():

    biggest = [1, 1]

    for i in range(2, 1000000):

        iter_list = []
        iter_list.append(i)

        while iter_list[-1] != 1:
            iter_list.append(collatz_iteration(iter_list[-1]))

        if len(iter_list) > biggest[1]:
            biggest[0] = i
            biggest[1] = len(iter_list)

    return biggest


if __name__ == "__main__":
	print(solution())