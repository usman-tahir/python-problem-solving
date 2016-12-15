
import Item

class Inventory:
    def __init__(self, space):
        self.space = space
        self.current_size = 0
        self.elements = []

    def add(self, item):
        if (self.space == self.current_size):
            print("There is no more space to store this item.")
        else:
            self.current_size += 1
            self.elements.append(item)
            print("A(n) %s has been added to the inventory." % (item.name))
            print(str(self.elements[self.current_size - 1]))
