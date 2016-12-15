
class Item:
    _global_id = 0
    def __init__(self, name, description, value = 0):
        self.item_id = (Item._global_id + 1)
        Item._global_id += 1
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        return "\nID: %d\nName: %s\nValue: %d\nDescription: %s" \
            % (self.item_id, self.name, self.value, self.description)
