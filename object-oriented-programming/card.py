
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def set_suit(self, suit):
        if suit.lower() not in ["hearts", "diamonds", "spades", "clubs"]:
            print("You did not specify a valid card suit.")
            return False
        else:
            self.suit = suit
            return True

    def set_value(self, value):
        if suit.upper() not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", \
            "10", "J", "Q", "K"]:
            print("You did not specify a valid card value.")
            return False
        else:
            self.value = value
            return True

    def full_value_name(self, value):
        if value in ["A", "J", "Q", "K"]:
            if value == "A":
                return "Ace"
            elif value == "J":
                return "Jack"
            elif value == "Q":
                return "Queen"
            else:
                return "King"
        else:
            return value

    def __str__(self):
        return (Card.full_value_name(self, self.value) + " of " + self.suit)
