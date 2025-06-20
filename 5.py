#basics yet importeant functions 

# print() function outputs the given message or data to the screen (standard output).
print("Hello, world!")  # Output: Hello, world!

#*************************------------------------------*****************************
# pow(base, exponent) function calculates the power of a number.
# It returns base raised to the exponent.

print(pow(2, 3))  # Output: 8  (2 raised to the power 3)

#*************************------------------------------*****************************
# Opens the file "file.txt" in read mode ("r"), reads its entire content into 'content', and then closes the file.

f = open("file.txt", "r")
content = f.read()
f.close()

#*************************------------------------------*****************************
# iter() creates an iterator from the list 'nums'.
# next() retrieves the next item from the iterator.

nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # Output: 1


#*************************------------------------------*****************************
# iter() creates an iterator from an iterable (like a list).
# next() returns the next item from the iterator each time it's called.

it = iter([10, 20])
print(next(it))  # Output: 10
print(next(it))  # Output: 20

#*************************------------------------------*****************************
# min() function returns the smallest value from the given iterable or arguments.

print(min([1, 5, 2]))  # Output: 1

#*************************------------------------------*****************************
# max() function returns the largest value from the given iterable or arguments.

print(max([1, 5, 2]))  # Output: 5

#*************************------------------------------*****************************
# locals() function returns a dictionary of the current local symbol table.
# It shows all local variables and their values within the current scope.

def demo():
    x = 10
    y = 20
    print(locals())  # Output: {'x': 10, 'y': 20}

demo()



#*************************------------------------------*****************************\
#binary number 
print(bin(10))  # Output: '0b1010' binary number 
#bool value
print(bool(0))    # Output: False
print(bool(5))    # Output: True for all non negative and positive integer ,except 0
print(bool(-5))   # Output: True for all non negative and positive integer ,except 0

#*************************------------------------------*****************************

# b = bytearray(b"hello") creates a mutable sequence of bytes in Python.
# Unlike bytes (which is immutable), bytearray allows you to modify its contents after creation.
# It’s useful when you need to work with binary data that can change.

b = bytearray(b"hello") #creates Mutable sequence of bytes
b[0] = 72
print(b)  # Output: bytearray(b'Hello')


# bytes are immutable, meaning once created, their contents cannot be changed.
# This immutability makes bytes safe to use as fixed data, 
# helps avoid accidental modification, and allows them to be used as keys in dictionaries or elements in sets.
# If you need a mutable sequence of bytes, use bytearray instead.
b = bytes("hello", "utf-8")
print(b)  # Output: b'hello'


#*************************------------------------------*****************************
#checks whether a function is callable 
print(callable(len))       # Output: True
print(callable(5))         # Output: False

#*************************------------------------------*****************************
# ord() function returns the Unicode code point (integer) of a given character.

print(ord('A'))  # Output: 65

#*************************------------------------------*****************************
# chr() converts a Unicode code point (integer) to its corresponding character.
# 65 is the Unicode code point for 'A', so chr(65) returns 'A'.print(chr(65))  # Output: 'A'
print(chr(65))  # Output: 'A'
print(chr(65)+chr(77)+chr(65)+chr(78)) # Output: 'AMAN'

#output This repository is for python , The unicode would be different based on uppercase and lowercase letter 
print(
    chr(84) + chr(104) + chr(105) + chr(115) + chr(32) + chr(114) + chr(101) + chr(112) + 
    chr(111) + chr(115) + chr(105) + chr(116) + chr(111) + chr(114) + chr(121) + chr(32) + 
    chr(105) + chr(115) + chr(32) + chr(102) + chr(111) + chr(114) + chr(32) + chr(112) + 
    chr(121) + chr(116) + chr(104) + chr(111) + chr(110)
)

# complex() creates a complex number from two real numbers.
print(complex(1, 2))  # Output: (1+2j)

#*************************------------------------------*****************************
# dict() creates a dictionary, which is an unordered collection of key-value pairs.
# Each key maps to a value, allowing fast lookups.
# In this example, 'a' maps to 1 and 'b' maps to 2.
#Further Explaination in Hinglish
# dict ya dictionary ek aisi cheez hai jisme "key" aur "value" ka joda (pair) hota hai.
# Jaise school mein roll number (key) se student ka naam (value) milta hai.
# Yahan 'a' key hai, uski value 1 hai. 'b' ki value 2 hai.

d = dict(a=1, b=2)
print(d)  # Output: {'a': 1, 'b': 2}

#*************************------------------------------*****************************

# divmod(7, 3) returns (quotient, remainder) → (2, 1)
# 7 divided by 3 gives 2 as quotient and 1 as remainder.
print(divmod(7, 3))  # Output: (2, 1)

#*************************------------------------------*****************************

# enumerate() gives both index and value while looping over a list.
# Here, i is index (0, 1), and val is value ('a', 'b').
# Output:
# 0 a
# 1 b
for i, val in enumerate(['a', 'b']):
    print(i, val)
    
#*************************------------------------------*****************************

# eval() evaluates a string as a Python expression.
# In this case, it evaluates the string '1+2' as an expression.
print(eval('1+2'))  # Output: 3
print(eval("3 + 5"))  # Output: 8

#*************************------------------------------*****************************
# exec() allows running multiple Python statements written as a string.
# It's powerful and used in advanced situations like dynamic code execution.
code = """
a = 5
b = 10
print(a + b)
"""
exec(code)  # Output: 15


#*************************------------------------------*****************************

# filter() selects items from the list that satisfy a given condition.
# Here, it keeps only even numbers from the list nums.
#Further explaination in Hinglish
# filter() ek built-in function hai jo kisi condition (function) ke base par ek iterable (jaise list) ko filter karta hai.
# lambda x: x % 2 == 0 ka matlab hai: x even ho.
# filter() har element pe lambda apply karta hai, aur sirf wahi elements rakhta hai jinke liye condition True hoti hai.
# Final result ek filter object hota hai, jise list mein convert karke print karte hain.
nums = [1, 2, 3, 4]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))  # Output: [2, 4]


# float() converts a number or string to a floating-point number.
print(float(5))  # Output: 5.0
print(float('3.14'))  # Output: 3.14

# format() formats a value based on the specified format.
# Here, it formats 3.14159 as a float with 2 decimal places.
print(format(3.14159, "f"))  # Output: 3.14159
print(format(3.14159, ".2f"))  # Output: 3.14

# frozenset() creates an immutable set — a set that cannot be changed after creation.
# Useful when you want to use a set as a key in a dictionary or prevent accidental modification.

s = frozenset([1, 2, 3])


#*************************------------------------------*****************************

#Further explaination in Hinglish
# getattr(object, attribute_name) ek built-in function hai jo kisi object ka attribute dynamically access karta hai.
# Yahan:
# a ek object hai class A ka.
# 'x' ek string hai jo attribute ka naam batata hai.
# getattr(a, 'x') ka matlab hai: a.x ki value le aao.
# Output: 5, kyunki x = 5 class A mein define kiya gaya hai.

class A:
    x = 5

a = A()
print(getattr(a, 'x'))  # Output: 5


#*************************------------------------------*****************************

# globals() returns a dictionary of all globally defined variables and functions.
# Useful for dynamic access and debugging in advanced use cases.x = 10
x = 10
y = 20

print(globals())  # sabhi global variables dikhayega
print(globals()['x'])  # 'x' variable ki value lega = 10


#*************************------------------------------*****************************

# hasattr(object, 'attribute') checks if the given attribute exists in the object.
# Returns True if attribute is present, otherwise False.

class A:
    x = 5

a = A()
print(hasattr(a, 'x'))   # True, because 'x' exists in object a
print(hasattr(a, 'y'))   # False, because 'y' does not exist in object a

# hash() function kisi immutable object (jaise numbers, strings, tuples) ka unique integer hash value return karta hai.
# Ye hash value objects ko quickly compare karne aur data structures (like dictionaries, sets) mein use karne ke liye hoti hai.
print(hash(42))          # Integer ka hash value
print(hash("hello"))     # String ka hash value
print(hash((1, 2, 3)))   # Tuple ka hash value

# Note: Mutable objects (like list, dict) ka hash nahi hota, unpe hash() call karoge to error aayega.
# lst = [1, 2, 3]
# print(hash(lst))  # This will raise an error!


#*************************------------------------------*****************************

# help() function kisi bhi function, module, ya class ka documentation ya usage instructions show karta hai.
# Yeh beginners ke liye bahut useful hota hai programming seekhne mein.
# Example 1: Getting help on a built-in function
help(len) #This shows how the built-in len() function works.

# Example 2: Getting help on a module
import math
print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # 4.0

# Example 3: Getting help on a method of a string
text = "hello"
help(str.upper)
print(text)  # This shows details about the string method upper().

# Example 4: Getting help on your own function
def greet(name):
    """Greets a person with their name."""
    print(f"Hello, {name}!")

help(greet) #Shows the docstring (the comment inside triple quotes) you wrote for your function.


#*************************------------------------------*****************************


# hex() converts an integer to a hexadecimal string starting with '0x'.
# Here, 255 in decimal is '0xff' in hexadecimal.
print(hex(255))  # Output: '0xff'

#*************************------------------------------*****************************

# id() function returns the unique identity (memory address) of an object in Python.
# It helps to check if two variables point to the same object.
a = [1, 2, 3]
b = a
print(id(a))  # Example output: 140435823040960 (unique number)
print(id(b))  # Same as id(a), since b points to the same object

c = [1, 2, 3]
print(id(c))  # Different from id(a) and id(b), new object in memory


#*************************------------------------------*****************************
# input() function is used to take input from the user.
# It can take a string argument to display a prompt.
name = input("Hello Guys, My name is Aman, Please share this repos to someone who wants to learn python? ") 


#*************************------------------------------*****************************
#int() convert value to integer
print(int("10"))  # Output: 10

#*************************------------------------------*****************************
# oct() function converts an integer to its octal (base-8) string representation.
# The result starts with '0o' to indicate octal format.

print(oct(8))  # Output: '0o10'

#*************************------------------------------*****************************
#len() - returns length of any iterable or string
print(len("hello"))  # Output: 5

#*************************------------------------------*****************************
# list()- convert iterable to list
print(list("abc"))  # Output: ['a', 'b', 'c']

#*************************------------------------------*****************************
#tuple()- convert iterable to tuple 
# Tuple ek immutable sequence hota hai, jise modify nahi kiya ja sakta.
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

#*************************------------------------------*****************************
# type() - returns the type of object
print(type("hello"))  # Output: <class 'str'>   
print(type(5))  # Output: <class 'int'>

#*************************------------------------------*****************************
# sum()-sum the elemnts of iterable
print(sum([1, 2, 3]))  # Output: 6

#*************************------------------------------*****************************
#convert object into string
print(str(10))  # Output: '10'

#*************************------------------------------*****************************
#sorted()-convert iterable to sorted list
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

#*************************------------------------------*****************************
# set() function converts an iterable into a set, which is an unordered collection of unique elements.
# Duplicate elements are removed in the resulting set.

print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

#*************************------------------------------*****************************
# setattr(object, 'attribute', value) sets or creates an attribute on the given object dynamically.
# Here, attribute 'x' is added to object 'a' with the value 10.

class A:
    pass

a = A()
setattr(a, 'x', 10)
print(a.x)  # Output: 10

#*************************------------------------------*****************************
# zip() function multiple iterables ko element-wise pair karta hai.
# Matlab, pehle elements ko ek saath, doosre elements ko ek saath, aur aise hi aage.
a = [1, 2]
b = ['x', 'y']
print(list(zip(a, b)))  # Output: [(1, 'x'), (2, 'y')]

#*************************------------------------------*****************************
# The slice() function creates a slice object used for indexing and slicing sequences.
# It specifies start, stop, and step values to extract parts of a sequence.

# Example:
s = slice(1, 5, 2)
lst = [10, 20, 30, 40, 50, 60]
print(lst[s])  # Output: [20, 40]

#*************************------------------------------*****************************
# round() function rounds a number to the nearest integer or to the specified number of decimal places.

print(round(3.14159))      # Output: 3
print(round(3.14159, 2))   # Output: 3.14

#*************************------------------------------*****************************
# reversed() function returns an iterator that accesses the given sequence in reverse order.
# Converting it to a list shows the reversed sequence.

print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

#*************************------------------------------*****************************
# repr() function returns a string that represents a valid Python expression of the object.
# It often includes quotes for strings to show their exact form.

print(repr("hello"))  # Output: "'hello'"

#*************************------------------------------*****************************
# The for loop iterates over numbers generated by range(3), which are 0, 1, and 2.
# It prints each number on a new line.
# Output: 0 1 2
for i in range(3): 
    print(i)

#*************************------------------------------*****************************
# memoryview() provides a view object that allows access to the internal data of bytes-like objects without copying.
# Useful for efficient manipulation of binary data (advanced use).

data = bytearray(b'hello')
view = memoryview(data)
print(view[0])  # Output: 104 (ASCII of 'h')

