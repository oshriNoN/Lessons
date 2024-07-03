
def read_num():
    b = True
    
    while b:
        user_input = input("Enter a num from 1000 to 9999 ")
        try:
            int(user_input)
            b = False
        except:
            print("Invalid input, enter again")
    return int(user_input)

print(read_num())