x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)


# Test 2
z = Fraction(3,6)
print(z)  #should be 1/2
assert z == Fraction(1,2)