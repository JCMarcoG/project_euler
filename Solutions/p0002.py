# Solution to Problem 0002

def solution():
    fib_list = [1, 2]
    while fib_list[-1] < 4000000:
        fib_list.append(fib_list[-2] + fib_list[-1])
    ans = sum(x for x in fib_list[:-1] if (x % 2 == 0))
    return(ans)


if __name__ == "__main__":
	print(solution())