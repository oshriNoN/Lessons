def Factorial(a):
    sum = 1
    num = int(a)
    for i in range(1, num + 1):
        sum = sum * i
        print(sum)


if __name__ == '__main__':
    a = input("Enter an Integer: ")
    Factorial(a)
