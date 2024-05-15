'''
Player can:
    add money
    pull money for bets 
    add money from bet wins
    count money  
'''

class Bet():
    
    def __init__(self,money) -> None:
        self.money = int(money)

    def deposit_money(self, deposit):
        self.money = int(deposit) + self.money
    
    def draw_money(self, draw):
        self.money = self.money - int(draw)
        return draw

    def __str__(self) -> str:
        print(f"You have in total: {self.money}$")
