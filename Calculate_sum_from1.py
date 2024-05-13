import os
from Factorial import *


def Calculate(num):
    number = int(num)
    sum = number
    for x in range(1, number):
        sum =+ sum + x
    return sum


def calc2():
    # s: store sum of all numbers
    s = 0
    n = int(input("Enter number "))
    # run loop n times
    # stop: n+1 (because range never include stop number in result)
    for i in range(1, n + 1, 1):
        # add current number to sum variable
        s += i
    print("\n")
    print("Sum is: ", s)


def main():
    num = input("Enter a positive integer: ")
    output = Calculate(num)
    print(output)
    # calc2()


if __name__ == '__main__':
    main()
