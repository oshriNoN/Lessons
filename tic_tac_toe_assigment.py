import os
import sys

row_1 = ['', '', '']
row_2 = ['', '', '']
row_3 = ['', '', '']
counter = 0

## Set the list and change X and O in the position selected 
def play():
    global row_1
    global row_2
    global row_3
    pos = input_pos()
    # ifs will check if spot is empty - if it will play it
    ##first row
    if pos[0] == 1:
        if row_1[pos[1]] == '':
            row_1[pos[1]] = is_x()
        else: 
            print("### Position is already occupied! ###")
    ##second row
    if pos[0] == 2:
        if row_2[pos[1]] == '':
            row_2[pos[1]] = is_x()
        else:
            print("### Position is already occupied! ###")
    ##third row 
    if pos[0] == 3:
        if row_3[pos[1]] == '':
            row_3[pos[1]] = is_x()
        else:
            print("### Position is already occupied! ###")

# draw the game 
def draw_game(r1,r2,r3):
    print(r3)
    print(r2)
    print(r1)
    print('\n')

# First play is 'X' then altarnating between 'O' and 'X'
def is_x():
    global counter
    if counter % 2 == 0:
        counter +=1
        return 'X'
    else:
        counter +=1
        return 'O'

# draw static possible pick for the player 
def draw_pos():
    print("Pick a position to play:")
    print('| 7 |', '| 8 |', '| 9 |')
    print('| 4 |', '| 5 |', '| 6 |')
    print('| 1 |', '| 2 |', '| 3 |\n')

# Get the user position and return it in a (row, pos) tuple
def input_pos():
    pos = 0
    while type(pos) == str or not (pos <= 9 and pos >= 1):
        pos = (input())
        try:
            pos = int(pos)
        except:
            print("NOT A NUMBER")
            continue
        if pos > 9:
            print("Number should be between 1 - 9")
            continue
    if pos >=1 and pos <= 3:
        return (1, pos - 1)
    if pos >=4 and pos <= 6:
        return (2, pos - 4)
    if pos >=7 and pos <= 9:
        return (3, pos - 7)

# Check if all the lists are full and if so return true (main will end the game) 
def check_end_game(r1,r2,r3):
    f1, f2, f3 = False, False, False
    for i in r1:
        if i == '':
            print(i)
            f1 = False
            break
        else:
            f1 = True

    for j in r2:
        if j == '':
            f2 = False
            break
        else:
            f2 = True

    for k in r3:
        if k == '':
            f3 = False
            break
        else:
            f3 = True

    if f1 and f2 and f3:
        return True
    else:
        return False

# Check if theres a full row for either X or O
def check_row_win(row, side):
    if row[0] == row[1] == row[2] == side:
        print(f"Game finished '{side}' won! - row")
        return True

# Check if theres a full column for either X or 
def check_column_win(side):
    for i in range(0, 3):
        if row_1[i] == row_2[i] == row_3[i] == side:
            print(f"Game finished '{side}' won! - column")
            return True

# Check if theres a full cross for either X or O
def check_cross_win(side):
    if row_1[0] == row_2[1] == row_3[2] == side:
        print(f"Game finished '{side}' won! - cross") 
        return True
    if row_1[2] == row_2[1] == row_3[0] == side:
        print(f"Game finished '{side}' won! - cross") 
        return True
    
# Calls funcs for - cross, column or cross and checks if either is true (is so - main will end the game)
def check_win():
    # global row_1
    # global row_2
    # global row_3
    if check_row_win(row_1, 'X') or check_row_win(row_2, 'X') or check_row_win(row_3, 'X'):
        return True
    elif check_row_win(row_1, 'O') or check_row_win(row_2, 'O') or check_row_win(row_3, 'O'):
        return True
    elif check_column_win('X') or check_column_win('O'):
        return True
    elif check_cross_win('X') or check_cross_win('O'):
        return True
    else:
        return False


def main():
    while True:
        
        draw_pos() # Draw static possible positions to play
        draw_game(row_1, row_2, row_3) # Draw dynamic positions played 
        play() # Input frokm the user and apply it to the correct position

        if check_win(): # Call check_win() func and will exit the program if true 
            draw_game(row_1, row_2, row_3)
            sys.exit(0)
        if check_end_game(row_1, row_2, row_3): # Call check_end_game() func and will exit the program if true 
            draw_game(row_1, row_2, row_3)
            print("Game is finished - Tie!")
            sys.exit(0)


if __name__ == '__main__':
    try:
        main() 
    except KeyboardInterrupt: # Exit the program gracefully in case of keyboard interupt 
        print("EXIT")
        sys.exit(0)