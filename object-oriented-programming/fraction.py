
class Fraction:
    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom
        Fraction.simplify(self)

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def is_improper(self):
        return (self.numerator > self.denominator)

    def add(self, other_fraction):
        new_numerator = (self.numerator * other_fraction.denominator) \
            + (self.denominator * other_fraction.numerator)
        new_denominator = (self.denominator * other_fraction.denominator)

        return Fraction(new_numerator, new_denominator)

    def get_gcd(num_one, num_two):
        while num_one % num_two != 0:
            old_num_one = num_one
            old_num_two = num_two

            num_one = old_num_two
            num_two = old_num_one % old_num_two
        return num_two

    def get_reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def simplify(self):
        old_numerator = self.numerator
        old_denominator = self.denominator
        common = Fraction.get_gcd(old_numerator, old_denominator)

        self.numerator = old_numerator // common
        self.denominator = old_denominator // common

    def __eq__(self, other_fraction):
        first_number = self.numerator * other_fraction.denominator
        second_number = other_fraction.numerator * self.denominator

        return first_number == second_number

    def __str__(self):
        return (str(self.numerator) + "/" + str(self.denominator))

my_fraction = Fraction(3, 5)
print(str(my_fraction))
print(my_fraction.is_improper())
other_fraction = Fraction(1, 5)
added = my_fraction.add(other_fraction)
print(added)
added.simplify()
print(str(added))
print (Fraction(1, 3) == Fraction(1, 3))

# Test fraction simplification on init
test_fraction = Fraction(100, 150)
print(str(test_fraction))

# Reciprocal test
print(str(Fraction(2, 3).get_reciprocal()))
print(Fraction.get_gcd(2, 3))
