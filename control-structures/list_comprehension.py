
import math

squares_list = []
for x in range(1, 11):
    squares_list.append(math.pow(x, 2))
print(squares_list)

print("\n%s\n" % ("-" * 10))

squares_list_comprehension = [math.pow(x, 2) for x in range(1, 11)]
print(squares_list_comprehension)

print("\n%s\n" % ("-" * 10))

squares_list_comprehension_two = [math.pow(x, 2) for x in range(1, 11) if x % 2 != 0]
print(squares_list_comprehension_two)

print("\n%s\n" % ("-" * 10))

letter_list_comprehension = [c.upper() for c in "comprehension" if c not in "aeiou"]
print(letter_list_comprehension)
