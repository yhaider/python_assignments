# Assignment: Compare Arrays
# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
#
# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same."
#


#Compare Arrays

def comp(one, two): #defining with two arrays being inputted
    same = 0 #to keep track of amount of values that are the same
    if isinstance(one, list) and isinstance(two, list): #verifying that inputs are lists
        if len(one) >= len(two): #if the lengths of the arrays are diff you have to change the range
            for x in range(0,len(two)):
                if one[x] == two[x]:
                    same += 1
                else:
                    print "The lists are not the same."
                    break
            if same == len(one) and same == len(two):
                print "The lists are the same."
            else:
                print "The lists are not the same."
        elif len(two) > len(one):
            for x in range(0, len(one)):
                if one[x] == two[x]:
                    same += 1
                else:
                    print "The lists are not the same."
                    break
            if same == len(one) and same == len(two): #this verifies that the lists are exactly the same, as in the lengths are the same
                print "The lists are the same."
            else: #if one array is the same but is shorter and is missing values, then they technically are not the same
                print "The lists are not the same."
    else:
        print "You did not input valid lists/arrays."
