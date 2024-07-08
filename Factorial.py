def Factorial(a):
    sum = 1
    num = int(a)
    for i in range(1, num + 1):
        sum = sum * i
        print(sum)

def factorial_recursion(n):
    n = int(n)
    if n == 1:
        return 1
    else:
        res = n * factorial_recursion(n-1)
    return res


if __name__ == '__main__':
    a = input("Enter an Integer: ")
    # Factorial(a)
    print("recur:", factorial_recursion(a))
