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
Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string.
Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . )

Observations:
Exceptions not tested.

Docs:

"""


def consume_separators(idx, string, separators):
    """

    :param idx:
    :param string:
    :param separators:
    :return:
    """

    while idx < len(string) and string[idx] in separators:
        idx += 1
    return idx


def consume_until(idx, string, until):
    """

    :param idx:
    :param string:
    :param until:
    :return:
    """

    while idx < len(string) and string[idx] not in until:
        idx += 1
    return idx


def count_if_not_empty(word, counter):
    if word is not '':
        counter += 1
    return counter


def count_words(string):
    """
    Can be done easier with regexp.

    :param string:
    :return:
    """

    separators = [' ', ',', '.', ';', '?', '!']
    word = ''
    counter = 0

    idx = 0
    while idx < len(string):
        if string[idx].isalpha():
            word = word + string[idx]
            idx += 1
        elif string[idx] in separators:
            idx = consume_separators(idx, string, separators)
            counter = count_if_not_empty(word, counter)
            word = ''
        else:  # we found a character that is not alphanumeric or a separator
            idx = consume_until(idx, string, separators)
            idx = consume_separators(idx, string, separators)
            word = ''
    return counter


if __name__ == "__main__":

    print("Test case 1: {0}".format(count_words(" This is a string.") == 4))
    print("Test case 2: {0}".format(count_words("This is      another string.") == 4))
    print("Test case 2: {0}".format(count_words("....This is      another string.") == 4))
