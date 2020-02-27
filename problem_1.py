"""
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_ints(max_num, num):
    """
    Summing up integers divisible by num under max_num is
    equivalent to summing numbers from 1 to some limit value
    and then multiplying by the num.

    For example:
    max_num = 10
    num = 3
    limit = (10 - 1) // 3 = 3
    (1 + 2 + 3)*3 = 3 + 6 + 9 = 18
    (1 + 2 + 3) = 3*(3+1) // 2
    (3*(3+1) // 2) * 3 = 6*3 = 18

    :param max_num:
    :param num:
    :return:
    """
    limit = (max_num - 1) // num
    return (limit*(limit+1) // 2) * num


def main():
    num1, num2 = 3, 5
    max_num = 10

    # multiples of num1*num2 need to subtracted as they are double counted or summed
    res = sum_ints(max_num, num1) + sum_ints(max_num, num2) - sum_ints(max_num, num1 * num2)

    print("Find the sum of all the multiples of 3 or 5 below 1000.")
    print("Answer: {ans}".format(ans=res))


if __name__ == "__main__":
    main()