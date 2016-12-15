
class Item:
    _global_id = 0
    def __init__(self, name, description, value = 0, stackable = False):
        self.item_id = (Item._global_id + 1)
        Item._global_id += 1
        self.name = name
        self.value = value
        self.description = description
        self.stackable = stackable
        self.count = 1

    def add_to_stack(self):
        if (self.stackable == True):
            self.count += 1

    def __str__(self):
        output = '''\nID: %d\nName: %s\nValue: %d\nDescription: %s
Stackable: %s\nCount: %d''' % (self.item_id, self.name, \
        self.value, self.description, str(self.stackable), self.count)
        return output
