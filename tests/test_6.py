import sys
sys.path.insert(0, '/workspaces/refactor-ci/src/')
from cs132_HW1 import Fraction 
x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2, 3)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

#Test 6
beta = Fraction(3, -5)
print(beta)
print(beta.get_num())
print(beta.get_den())
assert beta == Fraction(-3, 5)
