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
Give a string that represents a polynomial (Ex: "3x ^ 3 + 5x ^ 2 - 2x - 5") and a number (whole or float).
Evaluate the polynomial for the given value.

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


def consume_digits(idx, polynomial):
    """

    :param idx:
    :param polynomial:
    :return:
    """

    number = 0
    while idx < len(polynomial) and polynomial[idx].isdigit():
        number = number * 10 + int(polynomial[idx])
        idx += 1
    return number, idx


def calculate(a, b, operation):
    """

    :param a:
    :param b:
    :param operation:
    :return:
    """

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '^':
        return a ** b
    else:
        raise SystemExit


def evaluate(value, polynomial):
    """

    :param value:
    :param polynomial:
    :return:
    """

    separators = [' ']
    operators_1 = ['+', '-']
    operators_2 = ['^', '*', '/']

    operator_1 = None
    operator_2 = None

    result = None
    partial_result = None

    idx = 0
    while idx < len(polynomial):

        if polynomial[idx] in separators:
            idx = consume_separators(idx, polynomial, separators)

        elif polynomial[idx].isdigit():
            number, idx = consume_digits(idx, polynomial)
            if operator_2 is not None:
                partial_result = calculate(partial_result, number, operator_2)
            else:
                partial_result = number

        elif polynomial[idx].isalpha():
            if operator_2 is not None:
                partial_result = calculate(partial_result, value, operator_2)
                operator_2 = None
            elif partial_result is not None:
                partial_result = calculate(partial_result, value, '*')
            else:
                partial_result = value
            idx += 1

        elif polynomial[idx] in operators_1:
            if operator_1 is None:
                result = partial_result
            else:
                result = calculate(result, partial_result, operator_1)
            operator_1 = polynomial[idx]
            operator_2 = None
            idx += 1

        elif polynomial[idx] in operators_2:
            operator_2 = polynomial[idx]
            idx += 1

        else:
            print("Unwanted character found")
            return None

    if result is None:
        return partial_result

    if partial_result is not None:
        return calculate(result, partial_result, operator_1)


if __name__ == "__main__":
    print("Test case 1: {0}".format(evaluate(1, "3x ^ 3 + 1 * x ^ 2 - 2x - 5") == 21))
    print("Test case 2: {0}".format(evaluate(1, "3x") == 3))
    print("Test case 3: {0}".format(evaluate(1, "x3") == 3))
    print("Test case 4: {0}".format(evaluate(1, "x") == 1))
    print("Test case 5: {0}".format(evaluate(1, "3x ^ 3") == 27))
