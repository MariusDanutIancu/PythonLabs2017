"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 2/4/2018
Version: 0.1
Status: Production

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

obs:
all(map(lambda x: number % x != 0, list(range(2, number // 2))))
    -> memory error for large numbers -> it does save a list
    -> does not treat negative numbers
    -> it does make a true/false list that is not needed in this case
    (we can stop the algoritm when we find a true value)

docs:
http://book.pythontips.com/en/latest/map_filter.html

"""


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


def list_of_primes(li):
    """

    :param li:
    :return:
    """

    # [i for i in li if is_prime(i)]
    return list(filter(lambda nr: is_prime(nr), li))


if __name__ == '__main__':
    print("Test case 1: {0}".format(list_of_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7]))
