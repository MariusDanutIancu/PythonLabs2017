"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 1/26/2018
Version: 0.1
Status: Production
Python version: 3.x

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Exercise
Find The largest common divisor of multiple numbers. Define a function with variable number of parameters to resolve this.

Observations:
The GCD operator is commutative and associative: gcd(a,b,c) = gcd(gcd(a,b),c) = gcd(a,gcd(b,c)).
Exceptions not tested.

Docs:
https://docs.python.org/2/library/functions.html#reduce Obs: moved to functools.
https://en.wikipedia.org/wiki/Greatest_common_divisor
https://en.wikipedia.org/wiki/Euclidean_algorithm
"""


def reduce(func, iterable):
    """

    :param func:
    :param iterable:
    :return:
    """

    it = iter(iterable)

    value = next(it)
    for element in it:
        value = func(value, element)

    return value


def gcd_div(a, b):
    """
    Greatest common divisor using division.

    :param a:
    :param b:
    :return:
    """

    while b != 0:
        t = b
        b = a % b
        a = t

    return a


def gcd_sub(a, b):
    """
    Greatest common divisor using subtraction.

    :param a:
    :param b:
    :return:
    """

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def gcd_rec(a, b):
    """
    Recursive greatest common divisor using division.

    :param a:
    :param b:
    :return:
    """

    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


def gcd(func=gcd_div, *input_list):
    """
    Input should actually be passed using a list but the exercise want it this way.

    :param func: Applied function
    :param input_list: Variable number of parameters
    :return:
    """

    return reduce(func, input_list)


if __name__ == '__main__':

    print("Test case 1: {0}".format(gcd(gcd_div, 1, 2, 3, 4, 5) == 1))
    print("Test case 2: {0}".format(gcd(gcd_sub, 1, 2, 3, 4, 5) == 1))
    print("Test case 3: {0}".format(gcd(gcd_rec, 1, 2, 3, 4, 5) == 1))
    print("Test case 4: {0}".format(gcd(gcd_div, 2, 4, 6, 8, 10) == 2))
    print("Test case 5: {0}".format(gcd(gcd_sub, 2, 4, 6, 8, 10) == 2))
    print("Test case 6: {0}".format(gcd(gcd_rec, 2, 4, 6, 8, 10) == 2))
