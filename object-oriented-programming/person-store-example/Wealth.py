
class Wealth:
    def __init__(self, amount = 0):
        self.amount = amount

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def __str__(self):
        print("Current wealth: %d" % (self.amount))
