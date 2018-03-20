"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 2/4/2018
Version: 0.1
Status: Production

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
"""


def order_tuples(tuple_list):
    """

    :param tuple_list:
    :return:
    """

    sorted_list = sorted(tuple_list, key=lambda x: x[1][2])
    return sorted_list


if __name__ == '__main__':
    print("Test case 1: {0}".format(order_tuples([('zbc', 'zbc'), ('abc', 'bcd'), ('abc', 'zza')]) ==
                                    [('abc', 'zza'), ('zbc', 'zbc'), ('abc', 'bcd')]))
