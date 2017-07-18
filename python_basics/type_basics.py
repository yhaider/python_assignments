# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#
# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
#
# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
#
# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."




#Filter by Type

def filter(val):
    if isinstance(val, str): #this evaluates if the inputted value is a string
        if len(val) >= 50: #if the length of the string is more than fifty, it will execute the stuff indented below
            print "Long sentence."
        else: #otherwise, it will do below
            print "Short sentence."
    elif isinstance(val, int): #this evaluates if the inputted value is an integer
        if val >= 100:
            print "That's a big number!"
        else:
            print "That's a small number."
    elif isinstance(val, list): #this evaluates if the inputted value is a list
        if len(val) >= 10:
            print "Big list!"
        else:
            print "Short list."
