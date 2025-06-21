# The following code causes a type error between a string 
# and an integer:

print("5 * 3 = " + str(5*3)) 


# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  