import math

n = 1
if n < 0:
    print("Sorry, the value is negative.")
else:
    print(math.sqrt(n))

print("\n%s\n" % ("-" * 10))

score = 85
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

print("\n%s\n" % ("-" * 10))

# Refactoring of the above if-else structure
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 70:
    print("D")
else:
    print("F")
