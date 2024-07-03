# Generate random int from 1000 to 9999
# Verify that the input is valid (range and type)
# user guesses 
# Print how many nums are correct 
# count the round
# run again 
# if all 4 guesses are correct - exit 

from random import randint

def read_num(): # read an input - try to convert it to int and return it
    b = True
    while b:
        user_input = input("Enter a number from 1000 to 9999 ")
        try:
            if int(user_input) < 1000 or int(user_input) > 9999:
                print("Invalid number, enter again")
            else:
                b = False
        except:
            print("Invalid input, enter again")
    
    return [x for x in str(user_input)]


def guess(generated_list, user_list):
    # return sum([1 if user_list[i] == generated_list[i] else 0 for i in range(len(user_list))])
    correct_guess = 0
    wrong_guess = 0
    for i in range(len(generated_list)):
        if user_list[i] == generated_list[i]:
            correct_guess += 1
        else:
            wrong_guess += 1
    return (correct_guess, wrong_guess)


def main():
    counter = 0
    correct_guess = 0
    generated_int = randint(1000, 9999)
    generated_list = [y for y in str(generated_int)] # convert the random int to a list 

    while correct_guess != 4:
        user_list = read_num()
        print(generated_list, user_list) # print for testing
        correct_guess, wrong_guess = guess(generated_list, user_list)
        print(f"Correct guesses: {correct_guess} \nWrong guesses: {wrong_guess}\n")
        counter += 1
    else:
        exit(f"Guessed the number {generated_int} correctly After {counter} guesses" )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()