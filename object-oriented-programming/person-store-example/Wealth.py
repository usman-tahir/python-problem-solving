
class Wealth:
    def __init__(self, amount = 0, units = "coins"):
        self.amount = amount
        self.units = units

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def __str__(self):
        print("Current wealth: %d %s" % (self.amount, self.units))

class StoreWealth(Wealth):
    def __init__(self, store_name, amount = 0, units = "coins"):
        Wealth.__init__(self, amount, units)
        self.store_name = store_name

    def deposit(self, amount):
        self.amount += amount
        print("%s just increased its wealth by %d %s." \
            % (self.store_name, amount, self.units))
        print("Current wealth: %d %s." % (self.amount, self.units))

    def withdraw(self, amount):
        if amount > self.amount:
            print("You cannot withdraw that much wealth from the store.")
        else:
            self.amount -= amount
            print("%s just decreased its wealth by %d %s." \
                % (self.store_name, amount, self.units))
            print("Current wealth: %d %s" % (self.amount, self.units))

class PersonWealth(Wealth):
    def __init__(self, person_name, amount = 0, units = "coins"):
        Wealth.__init__(self, amount, units)
        self.person_name = person_name

    def deposit(self, amount):
        self.amount += amount
        print("%s just increased their wealth by %d %s" \
            % (self.person_name, amount, self.units))
        print("Current wealth: %d %s" % (self.amount, self.units))

    def withdraw(self, amount):
        if amount > self.amount:
            print("%s does not have enough wealth to withdraw that much." \
                % (self.person_name))
        else:
            self.amount -= amount
            print("%s just decreased their wealth by %d %s." \
                % (self.person_name, amount, self.units))
            print("Current wealth: %d %s" % (self.amount, self.units))
