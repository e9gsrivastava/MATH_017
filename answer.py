
'''convert num to its spelling'''
from solver import solver


def answer():
    """all the numbers from 1 to 1000
    (one thousand) inclusive were written out in words,
    how many letters would be used"""

    return solver(1, 1000)


if __name__ == "__main__":
    print(answer())