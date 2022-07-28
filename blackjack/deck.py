from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        self.cards = self.__generate_cards()

    def __generate_cards(self):
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit, False)
                cards.append(card)

        shuffle(cards)
        return cards

    def take_one_card(self, faceoff):
        chosen_card = self.cards[-1]
        self.cards.remove(chosen_card)
        if not faceoff:
            chosen_card.flip()
        return chosen_card
