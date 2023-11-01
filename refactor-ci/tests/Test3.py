x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

# Test 3
# __sub__
z = x-y
print(z)
assert z == Fraction(-1,6)
# __mul__
z = x*y
print(z)
assert z == Fraction(1,3)
# __truediv__
# from __future__ import division  #this might need to be imported
z = x/y
print(z)
assert z == Fraction(3,4)