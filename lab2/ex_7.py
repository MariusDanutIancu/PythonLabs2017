"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 2/4/2018
Version: 0.1
Status: Production

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Write a function that receives as default a default x number equal to 1, a variable number of strings,
and a boolean flag set to True. For each character string, generate a list containing the characters that have the
ASCII divisible by x if the flag is set to True, otherwise it should contain characters that have the non-div ASCII
code. Example: x = 2, "test", "hello", "lab002", flag = False will return ([['e', 's'], ['e', 'o'], ['a']] . Note: The
function must return a variable number of lists that corresponds to the number of character strings
received as an input.

"""


def get_div_function(x, flag):
    """
    Returns the required function based on flag.

    :param x:
    :param flag:
    :return:
    """

    if flag:
        return lambda n: ord(n) % x == 0
    return lambda n: ord(n) % x != 0


def format_lists(x=1, flag=True, *input_strings):
    """

    :param x:
    :param flag:
    :param input_strings:
    :return:
    """

    div = get_div_function(x, flag)
    return [[letter for letter in m_string if div(letter)] for m_string in input_strings]


if __name__ == '__main__':
    print("Test case 1: {0}".format(format_lists(2, False, "test",
                                                 "hello", "lab002") == [['e', 's'], ['e', 'o'], ['a']]))
