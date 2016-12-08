
import card

class Deck:
    def __init__(self):
        self.contents = []
        for suit in ["hearts", "diamonds", "spades", "clubs"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", \
                "J", "Q", "K"]:
                self.contents.append(card.Card(value, suit))
        self.size = len(self.contents)

    def get_contents(self):
        return self.contents

    def get_size(self):
        return self.size

    def __str__(self):
        card_strings = []
        for c in self.contents:
            card_strings.append(card.Card.__str__(c))
        return card_strings

deck = Deck()
print(deck.get_size())
print(Deck.__str__(deck))
