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

# Test 4
# __gt__
assert (x > y) is False
# __ge__
assert (x >= y) is False
# __lt__
assert (x < y) is True
# __le__
assert (x <= y) is True
# __ne__
assert (x != y) is True
