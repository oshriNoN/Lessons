'''
Rules:

Player can bet before each round - cant bet over the max 
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
from keyboard import on_press

player_sum = 0
dealer_sum = 0

is_hold = False

is_bust = False

deck = Deck()
bet = Bet(100)

deck.shuffle_deck()

# Func to draw top card and remove it from the deck
def draw_and_remove(m_sum):
    print("Drew", deck.draw_top())
    if m_sum + (deck.draw_top().get_value()) > 21 and (deck.draw_top().get_value()) == 11:
        print("Ace counts as 1")
        m_sum = m_sum + 1
    else:
        m_sum = m_sum + (deck.draw_top().get_value())
    print("You are on", m_sum)
    deck.remove_card()
    is_in_hit = True
    # time.sleep(1.3)
    return m_sum


def play(m_sum):
    global is_bust
    global is_hold

    if m_sum == 21:
        is_hold = True ## ADD win by default 
        return m_sum
    
    if m_sum > 21:
        is_bust = True
        is_hold = False
        return m_sum
    
    ch_in = input("\nPress Enter to hit\tPress H to hold:\n") 
    if ch_in == "":
        m_sum = draw_and_remove(m_sum)
        return m_sum
    
    elif on_press('h'):
        print("You decided to hold on", m_sum)
        is_hold = True
        return m_sum


def dealer_draw_and_remove(m_sum):
    print("Dealer drew:", deck.draw_top())
    m_sum = m_sum + deck.draw_top().get_value()
    print("Dealer on:", m_sum)
    deck.remove_card()
    return m_sum
    
def dealer_play(dealer_sum):
    if(dealer_sum < 21):
        dealer_sum = dealer_draw_and_remove(dealer_sum)
        return dealer_sum
    if(dealer_sum > 21):
        print("Dealer lost with", dealer_sum)
        return dealer_sum
    

def player_win(m_sum, m_bet):
    global is_hold
    global is_bust
    global player_sum
    print("Player won with", m_sum)
    print("You won", int(m_bet)*2,"$")
    bet.deposit_money(int(m_bet)*2)
    print("You have in total", bet.money)
    player_sum = 0
    is_bust = False
    is_hold = False


def bet_money():
    print("You have", bet.money)
    current_bet = input("How much do you want to bet? ")
    if bet.money < int(current_bet):
        print("You only have", bet.money, "Do you want to go all in? (if so answer - yes)")
        all_in_answer = input()
        if all_in_answer.lower() == "yes":
            current_bet = bet.money
        else:
            bet_money()

    bet.draw_money(current_bet)
    return current_bet

def dealer_win(m_sum, dealer_sum, m_bet):
    global is_hold
    global is_bust
    global player_sum
    print("Dealer won with", dealer_sum)
    print("You had", m_sum)
    print("You lost", m_bet, "And now have", bet.money)
    player_sum = 0
    is_bust = False
    is_hold = False

try:
    while bet.money > 0:
    # Player plays
        while not is_hold:
            if player_sum == 0:
                current_bet = bet_money()
            if player_sum == 21:
                player_win(player_win, current_bet)
                break
            if player_sum > 21:
                dealer_win(player_sum, dealer_sum, current_bet)
                break
            else:
                player_sum = play(player_sum)

        #Dealer Plays
        while is_hold:
            dealer_sum = dealer_play(dealer_sum)
            time.sleep(0.5)
            if dealer_sum > 21:
                player_win(player_sum, current_bet)
                break
            if dealer_sum == 21:
                dealer_win(player_sum, dealer_sum, current_bet)
                break
except KeyboardInterrupt:
    exit()
# if __name__ == "__main__":
#     try:
#         main(is_hold, player_sum, dealer_sum)
#     except KeyboardInterrupt:
#         exit()