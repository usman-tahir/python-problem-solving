
my_set = {3, 6, "cat", 4.5, False}
print(my_set)

print(len(my_set))
print(False in my_set)
print("dog" in my_set)

your_set = {99, 3, 100}

print(my_set.union(your_set))
print(my_set | your_set)

print(my_set.intersection(your_set))
print(my_set & your_set)

print(my_set.difference(your_set))
print(my_set - your_set)

print({3, 100}.issubset(your_set))
print({3, 100}<=your_set)

my_set.add("house")
print(my_set)
my_set.remove(4.5)
print(my_set)
print(my_set.pop())
print(my_set)
my_set.clear()
print(my_set)
