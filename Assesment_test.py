
def PrintOnlyS():
    st = 'Print only the words that start with s in this sentence'
    for word in st.split():
        if word[0].lower() == "s":
            print(word)
        else:
            pass


def PrintEvenNum(num):
    for x in range(0, int(num)):
        if x % 2 == 0:
            print(x)
        else:
            pass


def ListComprehension(num):
    new_list = []
    for x in range(1, num):
        if x % 3 == 0:
            new_list.append(x)
        else:
            pass
    print(new_list)


def WordEven():
    st = 'Print every word in this sentence that has an even number of letters'
    for word in st.split():
        if len(word) % 2 == 0:
            print(f'{word} - even')
        else:
            pass


def FizzBuzz():
    for x in range(0, 101):
        if x < 3:
            print(x)
        elif (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)


def FirstLetter():
    st = 'Create a list of the first letters of every word in this string'
    print([word[0] for word in st.split()]) 


def foo(*args):
    print(args)
    return sum(args)


def UpperAndLowerCase(word):
    new_word = ''
    i = 0
    for letter in word:
        
        if i % 2 == 0:
            new_word = new_word + letter.upper()
        else:
            new_word = new_word + letter.lower()
        i += 1
    return new_word

def main():
    print(UpperAndLowerCase('asdbawawdasd'))


if __name__ == '__main__':
    main()