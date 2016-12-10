
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
    
    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand

    def get_score(self):
        return self.score

    def set_hand(self, hand):
        self.hand = hand

    def set_score(self, score):
        self.score = score
    
    def shuffle_hand(self):
        random.shuffle(self.hand)
        
    def show_hand(self):
        print("\n%s has the following cards:" % (self.name))
        for h in self.hand:
            print(h)

    def __str__(self):
        return "\nName: " + self.name + "\nScore: " + str(self.score)
