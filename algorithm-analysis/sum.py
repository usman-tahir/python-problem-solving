
import time

def elapsed(time_one, time_two):
    return time_two - time_one

def sum_of_n(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    end = time.time()
    print("this algorithm took %f seconds to run." % (elapsed(start, end)))
    return the_sum

def sum_of_n_2(n):
    start = time.time()

    result = (n * (n + 1) / 2)

    end = time.time()

    print("this algorithm took %f seconds to run." % (elapsed(start, end)))
    return result


for x in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    sum_one = sum_of_n_2(x)
    print(sum_one)
