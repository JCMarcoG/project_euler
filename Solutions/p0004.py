# Solution to Problem 0004

def solution():
    palindromes = [0]
    for i in range(100,1000):
        for j in range(100,1000):
            if (str(i*j) == str(i*j)[::-1]) and (i*j > palindromes[-1]):
                palindromes.append(i*j)

    return palindromes[-1]


if __name__ == "__main__":
	print(solution())