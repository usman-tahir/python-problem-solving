
import Item

class Inventory:
    def __init__(self, space):
        self.space = space
        self.current_size = 0
        self.elements = []

    def search(self, item_name):
        found = False
        index = 0
        for i in range(len(self.elements)):
            if (self.elements[i].name.lower() == item_name.lower()):
                found = True
                index = i
                break
        result = [found, index]
        return result

    def add(self, item):
        if Inventory.is_full(self):
            print("There is no more space to store this item.")
        else:
            self.current_size += 1
            self.elements.append(item)
            print("A(n) %s has been added to the inventory." % (item.name))

    def remove(self, item_name):
        result_index = Inventory.search(self, item_name)
        removed = False

        if result_index[0] == True:
            self.elements.pop(result_index[1])
            self.current_size -= 1
            removed = True

        if removed:
            print("The %s has been removed from the inventory." \
                % (item_name.lower()))
        else:
            print("The inventory does not contain a %s" % (item_name.lower()))

    def is_full(self):
        return self.current_size == self.space
