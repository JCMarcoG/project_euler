# Solution to Problem 0005

import math
from utils import lcm

def solution():

    n = 1

    for i in range(1, 21):
        n = lcm(n, i)

    return n


if __name__ == "__main__":
	print(solution())