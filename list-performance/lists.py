from timeit import *

def test_one():
    l = []
    for i in range(1000):
        l = l + [i]

def test_two():
    l = []
    for i in range(1000):
        l.append(i)

def test_three():
    l = [i for i in range(1000)]

def test_four():
    l = list(range(1000))

t1 = Timer("test_one()", "from __main__ import test_one")
print("concat:", t1.timeit(number = 1000), "milliseconds\n")

t2 = Timer("test_two()", "from __main__ import test_two")
print("append:", t2.timeit(number = 1000), "milliseconds\n")

t3 = Timer("test_three()", "from __main__ import test_three")
print("list comprehension:", t3.timeit(number = 1000), "milliseconds\n")

t4 = Timer("test_four()", "from __main__ import test_four")
print("list range:", t4.timeit(number = 1000), "milliseconds\n")
