"""
Author: Marius-Danut Iancu
Email:  marius.danut94@outlook.com
Creation date (mm-dd-yyyy): 2/4/2018
Version: 0.1
Status: Production

A. I. CUZA UNIVERSITY OF IAŞI
Faculty of Computer Science Iasi

Write a function that receives a variable number of lists and returns a list of tuples as follows:
the first tuple contains the first items in the lists, the second element contains the items
on the position 2 in the lists, etc.
Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1.5, a " , 6, "b"), (3,7, "c")].
Note: If input lists do not have the same number of items, missing items will be replaced with None to be able
to generate max ([len(x) for x in input_lists]) tuples.

"""


def format_lists(*input_lists):
    """

    :param input_lists:
    :return:
    """

    my_max_range = max([len(list) for list in input_lists])
    result = [tuple(list[idx] if idx < len(list) else None for list in input_lists) for idx in range(my_max_range)]
    return result


if __name__ == '__main__':
    print("Test case 1: {0}".format(format_lists([1, 2, 3, 4], [5, 6, 7, 5, 6, 7, 8, 9], ["a", "b", "c", "d"]) ==
                                    [(1, 5, 'a'), (2, 6, 'b'), (3, 7, 'c'), (4, 5, 'd'),
                                     (None, 6, None), (None, 7, None), (None, 8, None), (None, 9, None)]))
