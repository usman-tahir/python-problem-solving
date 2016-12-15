
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

    def remove(self, name):
        removed = False
        for i in range(len(self.elements)):
            if self.elements[i].name.lower() == name.lower():
                self.elements.pop(i)
                self.current_size -= 1
                removed = True
                break
        if removed:
            print("The %s has been removed from the inventory." \
                % (name.lower()))
        else:
            print("The inventory does not contain a %s" % (name))
