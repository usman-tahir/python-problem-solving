
import Wealth

class Person:
    def __init__(self, name):
        self.name = name
        self.wealth = Wealth.PersonWealth(name, 0, "dollars")
        # print(type(self.wealth)) -> <'instance'>

    def deposit(self, amount):
        self.wealth.deposit(amount)

    def withdraw(self, amount):
        self.wealth.withdraw(amount)
