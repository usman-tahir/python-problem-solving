
import Wealth

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.wealth = Wealth.StoreWealth(store_name)

    def deposit(self, amount):
        self.wealth.deposit(amount)

    def withdraw(self, amount):
        self.wealth.withdraw(amount)
