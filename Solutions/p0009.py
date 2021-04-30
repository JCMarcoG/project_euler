# Solution to Problem 0009

from math import sqrt

def solution():

    i = 1
    j = 1

    while True:
        for j in range(1, i):
            c = sqrt(i**2 + j**2)
            if c == int(c):
                if i+j+c == 1000:
                    return i*j*c
        i += 1


if __name__ == "__main__":
	print(solution())