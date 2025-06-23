# Logical operators are used to combine conditional statements (True/False).
# 'and' returns True only if both conditions are True.
# 'or' returns True if at least one condition is True.
# 'not' reverses the result: True becomes False, and False becomes True.


# and operator
print(True and True)    # True
print(True and False)   # False

# or operator
print(True or False)    # True
print(False or False)   # False


# not operator
print(not True)         # False
print(not False)        # True

# Mixed example
a = 10
b = 5
print(a > b and b > 2)     # True
print(a < b or b == 5)     # True
print(not (a == 10))       # False
