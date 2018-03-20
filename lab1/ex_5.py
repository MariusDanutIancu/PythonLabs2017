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
Write a function that checks whether a character string contains special characters (\r, \t, \n, \a, \b, \f, \v)

Observations:
Exceptions not tested.

Docs:
https://docs.python.org/2.0/ref/strings.html

"""


def has_special_characters(string):
    """

    :param string:
    :return:
    """

    special_characters = ['\r', '\t', '\n', '\a', '\b', '\f', '\v']
    for character in string:
        if character in special_characters:
            return True
    return False


if __name__ == "__main__":
    print("Test case 1: {0}".format(has_special_characters("No special characters.") is False))
    print("Test case 2: {0}".format(has_special_characters("Special characters. \n") is True))
    print("Test case 3: {0}".format(has_special_characters(r"Special characters. \n") is False))
    print("Test case 4: {0}".format(has_special_characters(b"Special characters. \n") is False))
