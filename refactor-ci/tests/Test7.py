x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

#Test 7 radd
print(x + 1)
print(1 + x)
assert (x + 1) == Fraction(3,2)
assert (1 + x) == Fraction(3,2)
