"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 2/4/2018
Version: 0.1
Status: Production

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Write a function to return a list of the first n numbers in the Fibonacci string.

Obs:
One more way to generate fibonaci numbers is using perfect squares property

TODO: build a python generator to get the numbers
"""


def get_first_n_fibbonaci(n):
    """

    :param n:
    :return:
    """

    if n <= 0:
        return None
    if n == 1:
        return [0]

    fibonacci_list = [0, 1]
    idx = 2
    while idx < n:
        fibonacci_list.append(fibonacci_list[idx - 2] + fibonacci_list[idx - 1])
        idx += 1

    return fibonacci_list


if __name__ == '__main__':
    print("Test case 1: {0}".format(get_first_n_fibbonaci(1) == [0]))
    print("Test case 1: {0}".format(get_first_n_fibbonaci(2) == [0, 1]))
    print("Test case 1: {0}".format(get_first_n_fibbonaci(5) == [0, 1, 1, 2, 3]))
