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
Write a function that receives two strings as parameters and returns the number of occurrences of the first
character string in the second.

Observations:
Exceptions not tested.

Docs:

"""


def increment_values(a, b, c, count):
    """

    :param a:
    :param b:
    :param c:
    :param count:
    :return:
    """

    return a+count, b+count, c+count


def count_occurences(search, string):
    """
    Count word occcurences.

    :param search:
    :param string:
    :return:
    """

    counter = 0
    string_idx = 0
    while string_idx < len(string):

        search_idx = 0
        count_letters = 0
        while search_idx < len(search) and string_idx < len(string) and search[search_idx] == string[string_idx]:
            search_idx, string_idx, count_letters = increment_values(search_idx, string_idx, count_letters, 1)

        if count_letters == len(search):
            counter += 1
        elif count_letters == 0:
            string_idx += 1

    return counter


if __name__ == "__main__":
    print("Test case 1: {0}".format(count_occurences("abc", " aabc;xyz abcxyz abcxyz   abc xyz") == 4))
