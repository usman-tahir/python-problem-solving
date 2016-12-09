
import card
import player
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
        if self.size - number >= 0:
            for x in range(number):
                hand.append(card.Card.__str__(self.contents.pop()))
            self.size -= number
            print("There are now %d cards in the deck." % (self.size))
            return hand
        else:
            print("You cannot draw that amount of cards from the deck.")
            return hand

    def __str__(self):
        card_strings = []
        for c in self.contents:
            card_strings.append(card.Card.__str__(c))
        return card_strings

d = Deck()
d.shuffle()

p = player.Player()
p.set_hand(d.draw(2))
p.show_hand()
