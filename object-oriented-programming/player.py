
class Player:
    def __init__(self):
        self.hand = []
        self.score = 0

    def get_hand(self):
        return self.hand

    def get_score(self):
        return self.score

    def set_hand(self, hand):
        self.hand = hand

    def set_score(self, score):
        self.score = score

    def show_hand(self):
        print("This player has the following cards:")
        for h in self.hand:
            print(h)
