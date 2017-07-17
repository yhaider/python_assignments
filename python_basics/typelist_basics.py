#Type List

def typelist(val):
    total = 0
    string = "String: "
    strexist = 0 #This will keep track of if there are strings
    intexist = 0 #This will keep track of if there are numbers
    for x in val:
        if isinstance(x, str): #Checks if its a string
            string += x + " "
            strexist += 1
        elif isinstance(x, int): #Checks if its an integer
            total += x
            intexist += 1
        else:
            continue
    if strexist > 0 and intexist > 0: #Here is where we use those variables which kept track of the existence of strings and integers to determine what values to print
        print "The array you entered is of mixed type."
        print string
        print "Sum: " + str(total)
    elif strexist > 0 and intexist == 0:
        print "The array you entered is of string type."
        print string
    elif strexist == 0 and intexist > 0:
        print "The array you entered is of integer type."
        print "Sum:" + str(total)
    else:
        print "You have not inputted a valid array."
