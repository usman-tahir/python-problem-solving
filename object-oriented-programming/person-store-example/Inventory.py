
import Item

class Inventory:
    def __init__(self, space):
        self.space = space
        self.current_size = 0
        self.elements = []

    def search(self, item_name):
        found = False
        for i in range(len(self.elements)):
            if (self.elements[i].lower() == item_name.lower()):
                found = True
                break
        return found

    def add(self, item):
        if (self.space == self.current_size):
            print("There is no more space to store this item.")
        else:
            self.current_size += 1
            self.elements.append(item)
            print("A(n) %s has been added to the inventory." % (item.name))

    def remove(self, item_name):
        found = Inventory.search(item_name)
        removed = False

        if found:
            for i in range(len(self.elements)):
                if self.elements[i].name.lower() == item_name.lower():
                    self.elements.pop(i)
                    self.current_size -= 1
                    removed = True
                    break
        if removed:
            print("The %s has been removed from the inventory." \
                % (item_name.lower()))
        else:
            print("The inventory does not contain a %s" % (item_name.lower()))
