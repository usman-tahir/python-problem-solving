
import math

number = -112
try:
    print(math.sqrt(number))
except:
    print("Bad value for square root")
    print("using absolute value instead")
    print(math.sqrt(abs(number)))

print("\n%s\n" % ("-" * 10))
if number < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(number))
