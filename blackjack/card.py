class Card:
    # HEARTS = chr(9829)
    # DIAMONDS = chr(9830)
    # SPADES = chr(9824)
    # CLUBS = chr(9827)
    SUITS = [chr(9829), chr(9830), chr(9824), chr(9827)]
    NUMBER_RANKS = [str(rank) for rank in range(2, 11)]
    FACE_RANKS = ['J', 'Q', 'K', 'A']
    RANKS = NUMBER_RANKS + FACE_RANKS
    FACE_TYPES_VALUE = 10
    BLANK_VALUE = '#'
    MAX_PLAYER_POINT = 21

    def __init__(self, rank, suit, faceoff):
        self.suit = suit # hearts, diamons, spades, clubs
        self.rank = rank # 1-10, J, Q, K, A
        self.front_side = self.__generate_front_side()
        self.back_side = self.__generate_back_side()
        self.faceoff = faceoff
        self.current_side = self.back_side

    def __generate_back_side(self):
        return ' ___\n' +\
            f'|{Card.BLANK_VALUE * 2} |\n' + \
            f'|{Card.BLANK_VALUE * 3}|\n' + \
            f'|_{Card.BLANK_VALUE * 2}|'

    def __generate_front_side(self):
        return ' ___\n' +\
            f'|{self.rank.ljust(2)} |\n' + \
            f'| {self.suit} |\n' + \
            f"|_{self.rank.rjust(2, '_')}|"

    def flip(self):
        self.current_side = self.front_side if self.faceoff else self.back_side
