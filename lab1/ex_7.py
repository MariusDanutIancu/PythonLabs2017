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
Write a function that receives a char_len integer and a variable number of strings (strings) and check that each two
neighboring strings follow the following rule: the second string starts with the last char_len characters of the
first string (like the word game pheasant).

Observations:
Exceptions not tested.

Docs:

"""


def is_valid(char_len, *strings):

    for idx in range(1, len(strings)):
        if len(strings[idx-1]) < char_len and len(strings[idx]) < char_len:
            return False
        if strings[idx - 1][-char_len:] != strings[idx][:char_len]:
            return False
    return True


if __name__ == "__main__":
    print("Test case 1: {0}".format(is_valid(3, "abcd", "bcde") is True))
    print("Test case 1: {0}".format(is_valid(3, "abcde", "bcde") is False))
