# Solution to Problem 0006

def sum_square_first_n(n):
    s = n*(n+1)*(2*n+1)/6
    return s

def square_sum_first_n(n):
    s = (n*(n+1)/2)**2
    return s

def solution():

    return (square_sum_first_n(100) - sum_square_first_n(100))


if __name__ == "__main__":
	print(solution())