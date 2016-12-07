
def square(n):
    return n**2

def square_root(n):
    root = n / 2
    for k in range(20):
        root = (1 / 2) * (root + (n / root))
    return root

print(square(3))

print("\n%s\n" % ("-" * 10))

print(square(square(3)))

print("\n%s\n" % ("-" * 10))

print(square_root(9))

print("\n%s\n" % ("-" * 10))

print(square_root(3534))
