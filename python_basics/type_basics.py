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
