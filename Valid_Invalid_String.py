
valid = "T(hi)s (is (a) ((val)i)d (string))"


invalid = "(This is (an ((invalid) string)"




def is_valid_st(st):
    ctr_1 = 0
    ctr_2 = 0
    for l in st:
        if l == "(":
            ctr_1 +=1
        if l == ")":
            ctr_2 +=1
    if ctr_1 == ctr_2:
        return split_st(st)
    else:
        return False


def split_st(st):
    dic = {}
    final_lst = []
    counter = 0
    dic_pos = 0
    for index, l in enumerate(st):
        if l == "(":
            diff = 1
            counter = 1
            dic[dic_pos] = [index, 0]

            while diff != 0:
                if st[index + counter] == "(":
                    diff += 1

                if st[index + counter] == ")":
                    diff -= 1

                counter +=1
            else: 
                dic[dic_pos] = [index, index+counter]
                dic_pos +=1

    for key, value in dic.items():
        a,b = value
        final_lst.append((st[a:b]))
    return final_lst


def split_st2(st):
    
    stack = []
    substrings = []
    for i, c in enumerate(st):
        
        if c == "(":
            
            stack.append(i)
        
        if c == ")":
            
            if len(stack) == 0:
                
                raise Exception("Invalid string")

            idx = stack.pop()
            
            substring = st[idx: i + 1]
            substrings.append(substring)
    
    if len(stack) != 0:
        raise Exception("Invalid string")
    
    return substrings


try:
    print(is_valid_st(valid))
    print(split_st2(valid))
except KeyboardInterrupt:
    exit()
    


    