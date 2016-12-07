
print("Hello")
print("Hello", "World")
print("Hello", "World", sep='***')
print("Hello", "World", end='***')
print("\n")

name = "Usman"
age = 22
print(name, "is", age, "years old.")
print("%s is %d years old" % (name, age))

price = 24
item = "Banana"
print("The %s costs %d cents" % (item, price))
print("The %+10s costs %5.2f cents" % (item, price))
print("The %+10s costs %10.2f cents" % (item, price))

item_dict = {"item": "banana", "cost": 24}
print("The %(item)s costs %(cost)7.1f cents" % (item_dict))
