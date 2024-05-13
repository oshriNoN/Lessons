import math
import string

def sphere_volume(radius):
    return((4/3) * math.pi * math.pow(radius, 3))


def is_num_in_range(num, low, high):
    return num in range(low, high+1)


def high_low_string(st):
    up_count = 0
    low_count = 0
    for letter in st:
        if letter.isupper():
            up_count += 1
        elif letter.islower():
            low_count += 1
    return (low_count, up_count)


def unique_from_a_list(m_list):
    new_list = []
    for x in m_list:
        if x not in new_list:
            new_list.append(x)

    return new_list


def multiply_list(m_list):
    x = 1
    for num in m_list:
        x = x * num
    return x


def is_palindrome(st):
    new_st = st[::-1].replace(' ', '')
    return new_st == st.replace(' ', '')
    

def is_pangram(st):
    out_st = ''
    new_st = st.lower()
    new_st = (sorted(new_st.replace(' ', '')))
    print(new_st)
    for letter in new_st:
        if letter not in out_st:
            out_st = out_st + letter
    return out_st == string.ascii_lowercase


def main():
    # print(sphere_volume(4))
    # print(is_num_in_range(3,2,5))
    # print(high_low_string('Hello Mr. Rogers, how are you this fine Tuesday?'))
    # print(unique_from_a_list([1,1,1,2,2,2,3,3,4,5,5,5]))
    # print(multiply_list([1, 2, 3, -4]))
    # print(is_palindrome('race car'))
    print(is_pangram('The quick brown fox jumps over the lazy dog'))


if __name__ == '__main__':
    main()