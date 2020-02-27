"""
Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math


def perm(remainder, nums):
    """
    If the fist digit selected, then the last nine digits can be ordered in 9! = 362880 ways.
    So the first 362880 permutations start with a 0. The permutations from 362881 to 725760 start with a 1,
    and the permutations from 725761 to 1088640 starts with a 2. Based on this, the number must start with a 2.
    The division of max number by the remaining factorial gives the remainder, which is used for finding
    the next digit for the final answer.

    For example:
    First digit: 999999/9! = 2 with 274239 remainder. First digit is at index 2 (starting from 0), hence 2
    2 [0 1 3 4 5 6 7 8 9]
    Second digit: 274239/8! = 6 with 32319 remainder. Second digit is at index 6 hence 7
    2 7 [0 1 3 4 5 6 8 9]
    Third digit: 32319/7! = 6 with 2079 remainder. Third digit is at index 6 hence 8
    2 7 8 [0 1 3 4 5 6 9]
    Fourth digit: 2079/6! = 2 with 639 remainder. Fourth digit is at index 2 hence 3
    2 7 8 3 [0 1 4 5 6 9]

    :param remainder:
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return nums
    i = remainder // math.factorial(len(nums)-1)
    remainder = remainder % math.factorial(len(nums)-1)
    return nums[i] + perm(remainder, nums[:i] + nums[i+1:])


def main():
    nums = '0123456789'
    remain = 10**6 - 1

    res = perm(remain, nums)

    print("What is the millionth lexicographic permutation of \nthe digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?")
    print("Answer: {ans}".format(ans=res))


if __name__ == "__main__":
    main()