"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 1/27/2018
Version: 0.1
Status: Production
Python version: 3.x

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Exercise:
Write a function that returns the largest prime number from a string given as a parameter or -1 if the
character string contains no prime number.
Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271

Observations:
Exceptions not tested.

Docs:

"""


def consume_digits(idx, polynomial):
    """

    :param idx:
    :param polynomial:
    :return:
    """

    number = 0
    while idx < len(polynomial) and polynomial[idx].isdigit():
        number = number * 10 + int(polynomial[idx])
        idx += 1
    return number, idx


def is_prime(number):
    """

    :param number:
    :return:
    """

    if number <= 1:
        return False
    max_value = number // 2 + 1
    for num in range(2, max_value):
        if number % num == 0:
            return False
    return True


def largest_prime(string):
    """

    :param string:
    :return:
    """

    idx = 0
    max_prime = -1
    while idx < len(string):
        if string[idx].isdigit():
            number, idx = consume_digits(idx, string)
            if is_prime(number):
                max_prime = number if number > max_prime else max_prime
        else:
            idx += 1
    return max_prime


if __name__ == "__main__":
    print("Test case 1: {0}".format(largest_prime("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda") == 271))
