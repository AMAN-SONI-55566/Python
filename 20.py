#branching with if else 
# 'if' checks a condition and runs code only if the condition is True.
# 'else' runs code if the 'if' condition is False.
# Branching lets your program make decisions and choose different actions.
# You can also use 'elif' for multiple conditions between 'if' and 'else'.

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be under 15 characters")
        else:
            print("Valid username")

# Now actually call the function outside to run it
hint_username("Aman Soni")   #result will be : Valid username 

