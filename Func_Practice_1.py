import random
import math

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        elif b > a:
            return a
    else:
        if a > b:
            return a
        elif b > a:
            return b


def animal_crackers(word):
    l_1 = word.lower()[0]
    l_2 = word.split()[1][0].lower()
    return l_1 == l_2
    

def makes_twenty(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    return n1 == 20 or n2 == 20 or n1 + n2 == 20


def capitileze_one_and_four(word):
    new_word = ''
    i = 0
    for letter in word:
        if i == 0 or i == 3:
            new_word = new_word + letter.upper()
        else:
            new_word = new_word + letter
        i += 1
    return new_word


def master_yoda(text):
    new_text = ''
    new_text = (text.split()[::-1])
    return (' '  .join(new_text))


def within_ten(num):
    ## Check if num is +-10 from 100 
    ## Or check if num is +-10 from 200 
    if abs(100 - num) <= 10 or abs((200 - num)) <= 10:
        return True
    else:
        return False 


def has_33(m_list):
    prev_num = None
    for num in m_list:
        if prev_num == num == 3:
            return True
        else:
            prev_num = num
    return False
        

def three_times_string(word):
    new_word = ''
    for letter in word:
        new_word = new_word + (letter*3)

    return new_word


def generate_num(min,max):
    return random.randint(min,max)


def blackjack():
    a = generate_num(1, 11)
    b = generate_num(1, 11)
    c = generate_num(1, 11)
    total = a + b + c
    print("Cards are: ", a, b, c)
    if total <= 21:
        return total
    elif total > 21 and a or b or c == 11:
        if total - 10 <= 21:
            return total - 10
        else:
            return 'BUST'


def summer_of_69(m_list):
    sum = 0

    wait_for_9 = False
    for num in m_list: 
        if num == 6:
            wait_for_9 = True

        if wait_for_9 == True and num == 9:
            wait_for_9 = False
 
        elif not wait_for_9:
            sum = sum + num

    return sum


def spy_007(m_list):
    b_1 = False
    b_2 = False
    b_3 = False
    last_pos = 0
    i = 0
    for num in m_list:
        i+=1
        if num == 0:
            if b_1 and i - last_pos == 1:
                b_2 = True
                last_pos = i
            else:
                b_1 = True
                last_pos = i
        elif num == 7:
            if b_2 and i - last_pos == 1:
                b_3 = True
                
    return (b_1, b_2, b_3)


def count_primes(num):
    m_list = []
    for n in range(3, int(num+1)):
        i = n
        for a in range(2, i+1):
            if a == i:
                m_list.append(a)
                print(a)
            if i % a == 0:
                break
            else:
                continue
    return m_list


def main():
    # print(animal_crackers('Levelheaded Llama'))
    print(count_primes(190))
    # print(capitileze_one_and_four('macdonald'))
    # print(within_ten(204))
    print(has_33([1,3,3,4,5]))
    # print(three_times_string('Mississippi'))
    # print(summer_of_69([1,2,6,4,9,1,2,6,2,3,4,9,10]))
    ################## Checks for 0-0-7 in a list 
    # v = spy_007([1,2,0,0,7,5])
    # if v == (True, True, True):
    #     print("007")
    # else:
    #     print("No")
    ##################
    # print(count_primes(int(101)))

if __name__ == '__main__':
    main() 