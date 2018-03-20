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
Write a function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

Observations:
Exceptions not tested.

Docs:
https://pythonadventures.wordpress.com/2010/09/27/stringbuilder/

"""


def convert_sequence_to_lowercase(idx, string, result):
    """

    :param idx:
    :param string:
    :param result:
    :return:
    """

    while idx < len(string) and string[idx].isupper():
        result.append(string[idx].lower())
        idx += 1
    return idx


def format_last_letter(result):
    """

    :param result:
    :param idx:
    :return:
    """

    letter = result[len(result) - 1]
    result[len(result) - 1] = '_'
    result.append(letter)


def convert(string):
    """

    :param string:
    :return:
    """

    idx = 0
    result = list()

    if string[idx].isupper():
        idx = convert_sequence_to_lowercase(idx, string, result)
        if idx > 1:
            format_last_letter(result)

    while idx < len(string):

        if string[idx].isupper():
            result.append('_')
            aux_idx = convert_sequence_to_lowercase(idx, string, result)
            if aux_idx > idx+1 and aux_idx != len(string):
                format_last_letter(result)
            idx = aux_idx
        else:
            result.append(string[idx])
            idx += 1

    return ''.join(result)


if __name__ == "__main__":
    print(convert("CamelCaseString"))
    print("Test case 1: {0}".format(convert("CamelCaseString") == 'camel_case_string'))
    print(convert("Camel2CaseString"))
    print("Test case 2: {0}".format(convert("Camel2CaseString") == 'camel2_case_string'))
    print(convert("CamelCaseSTRING"))
    print("Test case 3: {0}".format(convert("CamelCaseSTRING") == 'camel_case_string'))
    print(convert("CAMELCaseSTRING"))
    print("Test case 4: {0}".format(convert("CAMELCaseSTRING") == 'camel_case_string'))
    print(convert("CamelCASEString"))
    print("Test case 5: {0}".format(convert("CamelCASEString") == 'camel_case_string'))
