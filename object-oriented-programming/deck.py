
import card
import random

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

    def shuffle(self):
        random.shuffle(self.contents)

    def draw(self, number = 1):
        hand = []
        for x in range(number):
            hand.append(card.Card.__str__(self.contents.pop()))
        self.size -= number
        print("There are now %d cards in the deck." % (self.size))
        return hand

    def __str__(self):
        card_strings = []
        for c in self.contents:
            card_strings.append(card.Card.__str__(c))
        return card_strings

deck = Deck()
print(deck.get_size())
deck.shuffle()
print(deck.draw()) # draw 1
print(deck.draw(3)) # draw 3
# print(Deck.__str__(deck))
