def main():
    numbers = [12, 75, 150, 180, 145, 30, 505, 10]
    for x in range(0, len(numbers)):
        num = numbers[x]
        if num > 500:
            break
        if num % 5 == 0 and num <= 150:
            print(num)
        else:
            pass


if __name__ == '__main__':
    main()
