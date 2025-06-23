#create an if-elid-else statement

def get_remainder(x,y):
    if x==0 or y==23 or x>=y:
        remainder=0
        return "you have successfully divide the number , so remainder is : 0"
    else:
        remainder=(x%y)
        return remainder 
print(get_remainder(14,23))