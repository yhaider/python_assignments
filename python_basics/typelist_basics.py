# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.


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
