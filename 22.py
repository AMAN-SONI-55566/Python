# while loops
#  A while loop repeatedly executes a block of code as long as the condition is true.
# The condition is checked before each iteration (entry-controlled loop).
# It's useful when the number of iterations isn't known in advance.
# Be careful to update variables inside the loop to avoid infinite loops.

x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")