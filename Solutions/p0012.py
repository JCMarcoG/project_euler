# Solution to Problem 0012

from utils import decompose_factors_2

def solution():

    tri_nums = [1]
    factors = [1]
    i = 2

    while True:

        tri_nums.append(i + tri_nums[-1])
        i += 1

        factors.append(len(decompose_factors_2(tri_nums[-1])))

        if factors[-1] >= 250:
            break


    return tri_nums[-1]


if __name__ == "__main__":
	print(solution())