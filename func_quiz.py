import random

def capital_indexes(st):
    m_list = []
    for index, l in enumerate(st):
        if l.isupper():
            m_list.append(index)
    return m_list


def mid(st): #Returns the mid letter from a string
    if len(st) % 2 == 0:
        return ""
    else:
        return st[len(st) // 2]
    

def online_count(statuses):
    counter = 0
    for person,status in statuses.items():
        if status == "online":
            counter += 1
    return counter


def only_ints(a, b):
    return type(a) == type(b) == int


def double_letters(st):
    st = st.lower()
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            return True
    return False


def add_dots(st):
    new_st = st[0]
    for i in range(len(st)-1):
        new_st += "." + st[i+1] 
    return new_st 

def remove_dots(st):
    return st.replace(".","")


def is_anagram(st1, st2):
    return sorted(st1) == sorted(st2)


def flatten(ls):
    new_ls = []
    for i in ls:
        for j in i:
            new_ls.append(j)

    return new_ls


def largest_difference(ls):
    return max(ls) - min(ls)


def get_row_col(pos):
    return ( int(pos[1]) - 1, ord(pos[0]) - ord('A'))


def consecutive_zeros(binary_st): # returns the maximum amount of '0' in the input
    counter = 0
    max_counter = 0
    for i in range(len(binary_st)):
        if binary_st[i] == "0":
            counter += 1
            if counter >= max_counter:
                max_counter = counter 
        else:
            counter = 0
    return max_counter
            

def all_equal(ls): # returns true of all list objects equals 
    if not ls:
        return False
    else:
        first = ls[0]
    for item in ls:
        if item != first:
            return False
    return True


def convert(ls): # convert list of int/float to str
    return [str(x) for x in ls]


def zap(l1, l2):
    new_list = []
    for i in range(len(l1)):
        new_list.append((l1[i], l2[i]))
    return new_list


def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)
        
def param_count(*args, **kwargs):
    return len(args) + len(kwargs)

def format_number(num): #not working 
    st = str(num)
    new_num = ""
    for i in range(len(st), 0, -1):
        print(len(st) - i)
        if (len(st) - i) % 2 == 0:
            new_num += "," + st[len(st) - i]
        else:
            new_num += st[len(st) - i]
        print(new_num)

format_number(1200300)