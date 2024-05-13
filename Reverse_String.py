# Reversing the sting in one line
def Reverse_no_loop(str):
    return str[::-1]


# Reversing the string in a for loop
def Reverse_loop(str):
    reverse_str = ""
    for x in range(1, len(str)):
        reverse_str = reverse_str + str[-(x)]
    return reverse_str + str[0]


def main():
    str_in = input("Enter a String:\n")
    print(Reverse_loop(str_in))
    print(Reverse_no_loop(str_in))


if __name__ == '__main__':
    main()
