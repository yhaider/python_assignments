# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.


#Find Characters

def char(val, char): #defining function with inputs
    new = [] #setting up new array
    for x in val:
        if x.find(char) >= 0: #this is marking whether or not that character exists within that index
            new.append(x) #if it does, add it to the empty array
        else:
            continue
    if new != []: #so if character did exist, then we will print the array
        print new
    else: #if the function finds nothing with that character, we can let the user know
        print "Nothing containing character exists."
