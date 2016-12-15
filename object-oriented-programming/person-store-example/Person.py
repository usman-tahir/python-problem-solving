
import Wealth
import Inventory

class Person:
    def __init__(self, name):
        self.name = name
        self.wealth = Wealth.PersonWealth(name)
        self.inventory = Inventory.Inventory(10)

    def deposit(self, amount):
        self.wealth.deposit(amount)

    def withdraw(self, amount):
        self.wealth.withdraw(amount)
