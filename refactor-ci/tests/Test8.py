x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

#Test 8 iadd
for i in range(y.get_den()):
    x += i
    print(x)
assert x ==  Fraction(7,2)

