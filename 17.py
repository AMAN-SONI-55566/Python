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

#proper example------------>>
#logical and 
print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# Define country and city variables : logical or 
country = "United States"
city = "New York City"

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))  # True or True = True

# False or True returns True
print(country == "New York City" or city == "New York City")  # False or True = True

# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)  # True or False = True

# False or False returns False
print("B_name" > "C_name" or "B_name" < "A_name") # False or False = False

#logical not
# Test Example 1:

x = 2*3 > 6
print("The value of x is:")
print(x)

print("")  # Prints a blank line

print("The inverse value of x is:")
print(not x)

# |  
# |
today = "Monday"
print(not today == "Tuesday") 


# The "today" variable states today is Monday. This makes the comparison
# "today == Tuesday" False. The logical operator "not" inverts the False
# result to become True. In other words, this expression asks if it is
# false that today is not Tuesday. More succinctly, "not False" means 
# True."