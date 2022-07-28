from ctypes.wintypes import DOUBLE
import sys
from deck import Deck

class Action:
    HIT = 'H'
    STAND = 'S'
    DOUBLE = 'D'


class Blackjack:
    def __init__(self):
        self.player_money = 5000
        self.player_bet = 0
        self.deck = Deck()
        self.dealer_cards = []
        self.player_cards = []

    def execute(self):
        self.print_game_rules()

        while True:
            if self.player_money < 1:
                print('You are broke!')
                print("Good thing you weren't playing with real money.")
                print('Thanks for playing!')
                sys.exit()

            self.get_player_bet()
            self.draw_cards()

    def get_player_bet(self):
        user_input = input(f'How much do you bet? (1-{self.player_money}, or QUIT)\n>')
        if user_input.isdecimal() and (1 < int(user_input) <= self.player_money):
            self.player_bet = user_input
            print(f'Bet: {self.player_bet}')
        elif user_input.upper() in ['QUIT', 'Q']:
            sys.exit()
        else:
            print(f'Please enter a number from 1 to {self.player_money}\n')
            return self.get_player_bet()

    def calculate_points(self, cards):
        print('=================== FIRST TURN ===================')
        for _ in range(0, 2):
            self.dealer_cards.append(
                self.deck.take_one_card(False)
            )
            self.player_cards.append(
                self.deck.take_one_card(False)
            )
        self.dealer_cards[0].faceoff = True

    def draw_cards(self):
        pass

    def reset_round(self):
        self.dealer_cards = []
        self.player_cards = []

    def print_game_rules(self):
        print('''
            Blackjack, by Al Sweigart al@inventwithpython.com
            The classic card game also known as 21. (This version doesn't have
            splitting or insurance.)
            More info at: https://en.wikipedia.org/wiki/Blackjack
            View this code at https://nostarch.com/big-book-small-python-projects
            Tags: large, game, card game
        ''')
        print(f'''
            Blackjack, by Al Sweigart al@inventwithpython.com
            Rules:
                Try to get as close to 21 without going over.
                Kings, Queens, and Jacks are worth 10 points.
                Aces are worth 1 or 11 points.
                Cards 2 through 10 are worth their face value.
                (H)it to take another card.
                (S)tand to stop taking cards.
                On your first play, you can (D)ouble down to increase your bet
                but must hit exactly one more time before standing.
                In case of a tie, the bet is returned to the player.
                The dealer stops hitting at 17.
        ''')
        print(f'Money: {self.player_money}')

if __name__ == "__main__":
    blackjack = Blackjack()
    blackjack.execute()
