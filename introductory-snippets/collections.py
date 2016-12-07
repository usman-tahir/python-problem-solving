
my_list = [1, 3, True, 6.5]
print(my_list)

my_list = [0] * 6
print(my_list)

my_list = [1, 2, 3, 4]
a = my_list * 3
print(a)
my_list[2] = 45
print(a)
print(my_list)

my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)
my_list.insert(2, 4.5)
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(6.5))
print(my_list.index(4.5))
my_list.remove(6.5)
print(my_list)
del my_list[0]
print(my_list)

print((54).__add__(21))
