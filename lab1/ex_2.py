"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 1/26/2018
Version: 0.1
Status: Production
Python version: 3.x

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Exercise:
Write a function that calculates how many vowels are in a string.

Observations:
Vowels: a, e, i, o, u
Exceptions not tested.

Docs:

"""


def count_vowels(string):
    """
    Counts vowels.

    :param string:
    :return:
    """

    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in string:
        if letter in vowels:
            counter += 1

    return counter


if __name__ == "__main__":

    print("Test case 1: {0}".format(count_vowels("This is a string.") == 4))
    print("Test case 2: {0}".format(count_vowels("This is another string.") == 6))
