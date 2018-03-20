"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 2/4/2018
Version: 0.1
Status: Production

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Write a function that receives as parameters two lists a and b and returns:
(a intersected with b, a reunited with b, a - b, b - a)
"""


def list_ops(a, b):
    """

    :param a:
    :param b:
    :return:
    """

    a_reun_b = set(a + b)
    a_inter_b = list(filter(lambda x: x in a, b))  # checks if elems from a are in b
    a_sub_b = list(filter(lambda x: x not in b, a))  # checks if elems from a are not in b
    b_sub_a = list(filter(lambda x: x not in a, b))
    return a_reun_b, a_inter_b, a_sub_b, b_sub_a


if __name__ == '__main__':
    print("Test case 1: {0}".format(list_ops([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
                                    == ({1, 2, 3, 4, 5, 6, 7, 8}, [4, 5], [1, 2, 3], [6, 7, 8])))
