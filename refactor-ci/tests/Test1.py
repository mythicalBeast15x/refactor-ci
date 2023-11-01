x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

#Test 1
x.get_num()
assert x.get_num() == 1
y.get_den()
assert y.get_den() == 3
