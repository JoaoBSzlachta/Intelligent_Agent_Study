import random


class Cards:
    def __init__(self):
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.col4 = []
        self.col5 = []
        self.col6 = []
        self.hearts_deck = []
        self.diamonds_deck = []
        self.clubs_deck = []
        self.spades_deck = []

        self.deck = [
            ['A', 'HEARTS', 'RED', 'DOWN'],
            ['2', 'HEARTS', 'RED', 'DOWN'],
            ['3', 'HEARTS', 'RED', 'DOWN'],
            ['4', 'HEARTS', 'RED', 'DOWN'],
            ['5', 'HEARTS', 'RED', 'DOWN'],
            ['6', 'HEARTS', 'RED', 'DOWN'],
            ['7', 'HEARTS', 'RED', 'DOWN'],
            ['8', 'HEARTS', 'RED', 'DOWN'],
            ['9', 'HEARTS', 'RED', 'DOWN'],
            ['10', 'HEARTS', 'RED', 'DOWN'],
            ['J', 'HEARTS', 'RED', 'DOWN'],
            ['Q', 'HEARTS', 'RED', 'DOWN'],
            ['K', 'HEARTS', 'RED', 'DOWN'],

            # Diamonds (Red)
            ['A', 'DIAMONDS', 'RED', 'DOWN'],
            ['2', 'DIAMONDS', 'RED', 'DOWN'],
            ['3', 'DIAMONDS', 'RED', 'DOWN'],
            ['4', 'DIAMONDS', 'RED', 'DOWN'],
            ['5', 'DIAMONDS', 'RED', 'DOWN'],
            ['6', 'DIAMONDS', 'RED', 'DOWN'],
            ['7', 'DIAMONDS', 'RED', 'DOWN'],
            ['8', 'DIAMONDS', 'RED', 'DOWN'],
            ['9', 'DIAMONDS', 'RED', 'DOWN'],
            ['10', 'DIAMONDS', 'RED', 'DOWN'],
            ['J', 'DIAMONDS', 'RED', 'DOWN'],
            ['Q', 'DIAMONDS', 'RED', 'DOWN'],
            ['K', 'DIAMONDS', 'RED', 'DOWN'],

            # Clubs (Black)
            ['A', 'CLUBS', 'BLACK', 'DOWN'],
            ['2', 'CLUBS', 'BLACK', 'DOWN'],
            ['3', 'CLUBS', 'BLACK', 'DOWN'],
            ['4', 'CLUBS', 'BLACK', 'DOWN'],
            ['5', 'CLUBS', 'BLACK', 'DOWN'],
            ['6', 'CLUBS', 'BLACK', 'DOWN'],
            ['7', 'CLUBS', 'BLACK', 'DOWN'],
            ['8', 'CLUBS', 'BLACK', 'DOWN'],
            ['9', 'CLUBS', 'BLACK', 'DOWN'],
            ['10', 'CLUBS', 'BLACK', 'DOWN'],
            ['J', 'CLUBS', 'BLACK', 'DOWN'],
            ['Q', 'CLUBS', 'BLACK', 'DOWN'],
            ['K', 'CLUBS', 'BLACK', 'DOWN'],

            # Spades (Black)
            ['A', 'SPADES', 'BLACK', 'DOWN'],
            ['2', 'SPADES', 'BLACK', 'DOWN'],
            ['3', 'SPADES', 'BLACK', 'DOWN'],
            ['4', 'SPADES', 'BLACK', 'DOWN'],
            ['5', 'SPADES', 'BLACK', 'DOWN'],
            ['6', 'SPADES', 'BLACK', 'DOWN'],
            ['7', 'SPADES', 'BLACK', 'DOWN'],
            ['8', 'SPADES', 'BLACK', 'DOWN'],
            ['9', 'SPADES', 'BLACK', 'DOWN'],
            ['10', 'SPADES', 'BLACK', 'DOWN'],
            ['J', 'SPADES', 'BLACK', 'DOWN'],
            ['Q', 'SPADES', 'BLACK', 'DOWN'],
            ['K', 'SPADES', 'BLACK', 'DOWN']
        ]
        self.rejected_deck = []

    def shuffle_cards(self):
        random.shuffle(self.deck)

    def set_board(self):
        columns = [1, 2, 3, 4, 5, 6]
        for i, num_cards in enumerate(columns, start=1):
            for _ in range(num_cards):
                card = self.deck.pop()
                getattr(self, f"col{i}").append(card)
            if getattr(self, f"col{i}"):
                getattr(self, f"col{i}")[-1][3] = 'UP'
        return self.get_board_state()

    def get_board_state(self):
        return {
            'col1': self.col1,
            'col2': self.col2,
            'col3': self.col3,
            'col4': self.col4,
            'col5': self.col5,
            'col6': self.col6,
            'Hearts': self.hearts_deck,
            'Diamonds': self.diamonds_deck,
            'Clubs': self.clubs_deck,
            'Spades': self.spades_deck
        }

    def get_hierarchy_position(self, card):
        hierarchy = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
        return hierarchy.index(card)
