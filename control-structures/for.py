
for item in [1, 3, 6, 2, 5]:
    print(item)

print("\n%s\n" % ("-" * 10))

for item in range(5):
    print(item**2)

print("\n%s\n" % ("-" * 10))

word_list = ["cat", "dog", "rabbit"]
letter_list = []
for word in word_list:
    for letter in word:
        letter_list.append(letter)
print(letter_list)
