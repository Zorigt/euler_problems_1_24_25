# coding=utf-8
"""
Problem 25: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from math import log10, ceil, sqrt


def main():
    """
    Although this problem can be solved using dynamic programming by
    storing the fibonacci values in a list, it is more efficient in terms
    of memory and scalability to apply a known mathematical formula.
    Use Binet’s formula for finding the nth Fibonacci term.
    http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
    Use the ceiling function to find the closest integer.

    :return:
    """
    phi = (1 + sqrt(5)) / 2
    d = 1000
    term = ceil((log10(5) / 2 + d - 1) / log10(phi))

    print("What is the index of the first term in the Fibonacci sequence to contain 1000 digits?")
    print("Answer: {ans}".format(ans=int(term)))


if __name__ == "__main__":
    main()