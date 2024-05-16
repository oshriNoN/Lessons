'''
Rules:

Player can bet before each round 
If he bets over the max he goes all in instead
    1. player goes first:
        a. can hit or stay as much as he wants 
        b. if he hits above 21 - bust 
    2. Computer (dealer) goes second 
        a. if he equals or lessen than the player he loses 
        b. if he goes over 21 - bust 
    if the player wins he double his bets 

    * Ace can be either 11 or 1 
    * all face cards are 10 (J,Q,K)
'''
from Blackjack_Bets import Bet
from BlackJack_Deck import Deck
import time

player_sum = 0
dealer_sum = 0
is_hold = False #will change globaly if the player is holding or not

deck = Deck() #creates new deck 
bet = Bet(100) #create a bet with x money deposited


# Func to draw top card and remove it from the deck
def draw_and_remove(pl_sum):
    print("Drew", deck.draw_top())
    # If drew ACE and sum is more than 21 ace will count as one instead of 11 
    if pl_sum + (deck.draw_top().get_value()) > 21 and (deck.draw_top().get_value()) == 11:
        print("Ace counts as 1")
        pl_sum = pl_sum + 1
    else:
        pl_sum = pl_sum + (deck.draw_top().get_value())
    print("You are on", pl_sum)
    deck.remove_card()
    return pl_sum


def play(pl_sum):
    global is_hold
    if pl_sum == 21:
        is_hold = True # Wins by blackjack
        return pl_sum    
    if pl_sum > 21: # bust
        is_hold = True
        return pl_sum
    
    ch_in = input("\nPress Enter to hit\tPress H to hold:\n") 
    try:
        if ch_in == "":
            pl_sum = draw_and_remove(pl_sum)
            return pl_sum
        
        elif ch_in.lower() == ("h"):
            print("You decided to hold on", pl_sum)
            is_hold = True
            return pl_sum
    except:
        play()
    

def dealer_draw_and_remove(pl_sum):
    print("Dealer drew:", deck.draw_top())
    pl_sum = pl_sum + deck.draw_top().get_value()
    print("Dealer on:", pl_sum, "\n") 
    deck.remove_card()
    return pl_sum
    

def dealer_play(dealer_sum):
    if(dealer_sum < 21): 
        dealer_sum = dealer_draw_and_remove(dealer_sum)
        return dealer_sum
    if(dealer_sum > 21):
        print("Dealer lost with", dealer_sum)
        return dealer_sum
    if dealer_sum == 21:
        return dealer_sum


# Bet money, if you want to bet more than you have you will be asked if u want to go all in 
def bet_money() -> int:
    current_bet = 0
    print(f"\nYou have {bet.money}$")
    current_bet = input("How much do you want to bet? ")    
    
    try:
        int(current_bet)
    except:
        print("Invalid bet - bet again")
        bet_money()

    if bet.money <= int(current_bet):
        print("You only have", bet.money, "Do you want to go all in? (if so answer - yes)")
        all_in_answer = input()
        if all_in_answer.lower() == "yes":
            current_bet = bet.money
            bet.draw_money(bet.money)
            return current_bet
        else:
            bet_money()
    bet.draw_money(current_bet)
    return current_bet


def dealer_win(pl_sum, dl_sum, m_bet, bust=False):
    global is_hold
    global player_sum
    global dealer_sum
    if bust:
        print("Bust!")
    else:
        print("Dealer won with", dl_sum)
    print("You had", pl_sum)
    print(f"You lost {m_bet}$ And now have {bet.money}$")
    player_sum = 0
    dealer_sum = 0
    is_hold = False


def player_win(pl_sum, m_bet):
    global is_hold
    global player_sum
    global dealer_sum
    m_int_bet = int(m_bet)
    print("Player won with", pl_sum)
    print("You won:", m_int_bet * 2,"$")
    bet.deposit_money(m_int_bet * 2)
    print(f"You have in total {bet.money}$")
    player_sum = 0
    dealer_sum = 0
    is_hold = False


def main():
    global player_sum
    global dealer_sum
    global is_hold
    player_sum, dealer_sum = 0, 0
    
    deck.shuffle_deck() # Randomizes the deck's order

    # While player has money
    while bet.money > 0:
        # Player plays when -global- hold is false
        while not is_hold:
            if player_sum == 0:
                current_bet = bet_money()
            if player_sum == 21:
                print("BLACKJACK!")
                player_win(player_sum, m_bet=current_bet)
                break
            if player_sum > 21:
                dealer_win(player_sum, dealer_sum, m_bet=current_bet, bust=True)
                break
            else:
                player_sum = play(player_sum)

        #Dealer Plays
        while is_hold:
            dealer_sum = dealer_play(dealer_sum)
            time.sleep(0.5)
            if dealer_sum > 21:
                player_win(player_sum, m_bet=current_bet)
                break
            if dealer_sum >= player_sum < 21:
                dealer_win(player_sum, dealer_sum, m_bet=current_bet)
                break
            if dealer_sum == 21:
                print("BLACKJACK!")
                dealer_win(player_sum, dealer_sum, m_bet=current_bet)
                break
    else:
        print("Game finished")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()