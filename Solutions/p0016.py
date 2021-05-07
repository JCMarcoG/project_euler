# Solution to Problem 0015


def solution():

    suma = 0
    num = 2**1000

    num_str = str(num)

    for digit in num_str:
        suma += int(digit)

    return suma


if __name__ == "__main__":
	print(solution())