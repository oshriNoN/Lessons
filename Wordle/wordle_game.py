# Wordle game
# choose a random 5 letter word from a list 
# user input 
# verify word is valid - 5 letters (only)
# compare words 
# colour the correct letters with the correct position in green, correct letters wrong position in yellow
# game ends when the user guesses correct or after 6 guesses 

from words_list import words
from random import choice
from colorama import Fore # colouring the letters 

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
round_count = 6

def get_word_from_user():
    while True:
        user_word : str= input(f"{Fore.WHITE} Enter a 5 letter word to guess\n")
        if user_word.isalpha() and len(user_word) == 5: # Verify only letters and length of string is 5
            return user_word
        else:
            print("Invalid input")
            continue

# Not in use 
def get_ch_count(user_word, ch): 
    # Using a list to store the count of each alphabet
    # by mapping the character to an index value
    abc_list = [0] * 26
    # Storing the count
    for i in range(len(user_word)):
        abc_list[ord(user_word[i]) - ord('a')] += 1
    
    # Get count
    # print("The count of ", ch, " is ", abc_list[ord(ch) - ord('a')])
    return abc_list[ord(ch) - ord('a')]


def get_ch_pos(word, ch):
    # Using a list to store the locations of each alphabet
    # by mapping the character to an index value
    locations = {}
    # Storing the locations
    for j in range(len(word)):
        if word[j] not in locations:
            locations[word[j]] = []
        locations[word[j]].append(j)

    # Search the pos of the character
    try:
        # print("The locations of", ch, "is", locations[ch])
        return locations[ch]
    except KeyError:
        print("Not found")


def compare(random_word, user_word):
    if random_word == user_word:
        exit(f"{green} {user_word} is correct!")

    else:
        output_dic = {}
        for i in range(len(user_word)):
            if random_word.count(user_word[i]) > 0:
            # if get_ch_count(random_word, ch=user_word[i]) > 0: 
                pos_user = get_ch_pos(random_word, ch=user_word[i])
                pos_random = get_ch_pos(random_word, ch=random_word[i])
                if pos_user == pos_random:
                    output_dic[i] = (pos_user, green)
                else:
                    output_dic[i] = (pos_user, yellow)
            else:
                output_dic[i] = (i, red)
        return output_dic


def print_output(dic, user_word):
    st = ""
    for key, value in dic.items():
        st += f"{value[1]}{user_word[key]} "
    print(st)


def main():
    random_word = choice(words) # Generate random word
    i = 0 # Reset the counter 
    while i < round_count:
        user_word = get_word_from_user() 
        output_dic = compare(random_word, user_word) #
        print_output(output_dic, user_word)
        print(white, "\t")
        # print(random_word)
        i+=1
    else:
        print(f"{red} FAIL!{white} Word was:{red} {random_word}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
    
    


