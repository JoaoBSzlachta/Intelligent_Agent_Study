class Player:
    def __init__(self, cards, columns):
        self.cards = cards
        self.col1 = columns['col1']
        self.col2 = columns['col2']
        self.col3 = columns['col3']
        self.col4 = columns['col4']
        self.col5 = columns['col5']
        self.col6 = columns['col6']
        self.hearts = columns['Hearts']
        self.diamonds = columns['Diamonds']
        self.clubs = columns['Clubs']
        self.spades = columns['Spades']
        self.rejected_deck = cards.rejected_deck

    """Simple Reflex Agent"""
    def solitaire_player_SRA(self):
        while self.cards.deck:
            card = self.cards.deck.pop()
            card[3] = 'UP'
            print(f"Card: {card}")

            if not self.hearts and card[0] == 'A' and card[1] == 'HEARTS':
                self.hearts.append(card)
            elif not self.diamonds and card[0] == 'A' and card[1] == 'DIAMONDS':
                self.diamonds.append(card)
            elif not self.clubs and card[0] == 'A' and card[1] == 'CLUBS':
                self.clubs.append(card)
            elif not self.spades and card[0] == 'A' and card[1] == 'SPADES':
                self.spades.append(card)

            elif (self.hearts and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.hearts[-1][0]) -1)
                  and card[1] == 'HEARTS'):
                self.hearts.append(card)
            elif (self.diamonds and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.diamonds[-1][0]) -1)
                  and card[1] == 'DIAMONDS'):
                self.diamonds.append(card)
            elif (self.clubs and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.clubs[-1][0]) -1)
                  and card[1] == 'CLUBS'):
                self.clubs.append(card)
            elif (self.spades and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.spades[-1][0]) -1)
                  and card[1] == 'SPADES'):
                self.spades.append(card)
            else:
                if self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col1[-1][0]) + 1) and card[2] != self.col1[-1][2]:
                    self.col1.append(card)
                elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col2[-1][0]) + 1) and card[2] != self.col2[-1][2]:
                    self.col2.append(card)
                elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col3[-1][0]) + 1) and card[2] != self.col3[-1][2]:
                    self.col3.append(card)
                elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col4[-1][0]) + 1) and card[2] != self.col4[-1][2]:
                    self.col4.append(card)
                elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col5[-1][0]) + 1) and card[2] != self.col5[-1][2]:
                    self.col5.append(card)
                elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col6[-1][0]) + 1) and card[2] != self.col6[-1][2]:
                    self.col6.append(card)
                else:
                    self.rejected_deck.append(card)
                    print("It was not able to place the card!\n")

                print(f"Col1: {self.col1}")
                print(f"Col2: {self.col2}")
                print(f"Col3: {self.col3}")
                print(f"Col4: {self.col4}")
                print(f"Col5: {self.col5}")
                print(f"Col6: {self.col6}\n")

            print(f"Hearts: {self.hearts}")
            print(f"Diamonds: {self.diamonds}")
            print(f"Clubs: {self.clubs}")
            print(f"Spades: {self.spades}")

        print(f"Deck: {self.cards.deck}")
        print(f"Rejected Deck: {self.rejected_deck} \n")
        print(f"Col1: {self.col1}")
        print(f"Col2: {self.col2}")
        print(f"Col3: {self.col3}")
        print(f"Col4: {self.col4}")
        print(f"Col5: {self.col5}")
        print(f"Col6: {self.col6}\n")
        print(f"Hearts: {self.hearts}")
        print(f"Diamonds: {self.diamonds}")
        print(f"Clubs: {self.clubs}")
        print(f"Spades: {self.spades}")

    """Model-based Reflex Agent"""
    def solitaire_player_MbRA(self):
        attempts = 0
        while True:
            cards_are_placed = False
            if not self.cards.deck:
                self.cards.deck = self.rejected_deck
                self.rejected_deck = []

            while self.cards.deck:
                card = self.cards.deck.pop()
                card[3] = 'UP'
                print(f"Card: {card}")
                placed = False

                if not self.hearts and card[0] == 'A' and card[1] == 'HEARTS':
                    self.hearts.append(card)
                    placed = True
                elif not self.diamonds and card[0] == 'A' and card[1] == 'DIAMONDS':
                    self.diamonds.append(card)
                    placed = True
                elif not self.clubs and card[0] == 'A' and card[1] == 'CLUBS':
                    self.clubs.append(card)
                    placed = True
                elif not self.spades and card[0] == 'A' and card[1] == 'SPADES':
                    self.spades.append(card)
                    placed = True

                elif (self.hearts and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.hearts[-1][0]) -1)
                      and card[1] == 'HEARTS'):
                    self.hearts.append(card)
                    placed = True
                elif (self.diamonds and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.diamonds[-1][0]) -1)
                      and card[1] == 'DIAMONDS'):
                    self.diamonds.append(card)
                    placed = True
                elif (self.clubs and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.clubs[-1][0]) -1)
                      and card[1] == 'CLUBS'):
                    self.clubs.append(card)
                    placed = True
                elif (self.spades and self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.spades[-1][0]) -1)
                      and card[1] == 'SPADES'):
                    self.spades.append(card)
                    placed = True
                else:
                    if self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col1[-1][0]) + 1) and card[2] != self.col1[-1][2]:
                        self.col1.append(card)
                        placed = True
                    elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col2[-1][0]) + 1) and card[2] != self.col2[-1][2]:
                        self.col2.append(card)
                        placed = True
                    elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col3[-1][0]) + 1) and card[2] != self.col3[-1][2]:
                        self.col3.append(card)
                        placed = True
                    elif self.cards.get_hierarchy_position(card[0]) == (self.cards.get_hierarchy_position(self.col4[-1][0]) + 1) and card[2] != self.col4[-1][2]:
                        self.col4.append(card)
                    elif self.cards.get_hierarchy_position(card[0]) == (
                            self.cards.get_hierarchy_position(self.col5[-1][0]) + 1) and card[2] != self.col5[-1][2]:
                        self.col5.append(card)
                    elif self.cards.get_hierarchy_position(card[0]) == (
                            self.cards.get_hierarchy_position(self.col6[-1][0]) + 1) and card[2] != self.col6[-1][2]:
                        self.col6.append(card)
                    else:
                        self.rejected_deck.append(card)
                        print("It was not able to place the card!\n")
                if placed:
                    cards_are_placed = True
                    print(f"Col1: {self.col1}")
                    print(f"Col2: {self.col2}")
                    print(f"Col3: {self.col3}\n")

                print(f"Hearts: {self.hearts}")
                print(f"Diamonds: {self.diamonds}")
                print(f"Clubs: {self.clubs}")
                print(f"Spades: {self.spades}")

            if not cards_are_placed:
                print(f"\n========================================The End of Attempt {attempts}========================================")
                print("\nTrying again...")
                attempts += 1

            if attempts > 2:
                print("There is no more cards to be moved. The game is over! \n")
                print(f"Deck: {self.cards.deck}")
                print(f"Rejected Deck: {self.rejected_deck} \n")
                print(f"Col1: {self.col1}")
                print(f"Col2: {self.col2}")
                print(f"Col3: {self.col3}")
                print(f"Col4: {self.col4}")
                print(f"Col5: {self.col5}")
                print(f"Col6: {self.col6}\n")
                print(f"Hearts: {self.hearts}")
                print(f"Diamonds: {self.diamonds}")
                print(f"Clubs: {self.clubs}")
                print(f"Spades: {self.spades}")
                break
