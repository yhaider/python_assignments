# Assignment: Fun with Functions
# Create a series of functions based on the below descriptions.
#
# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
#
# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument.
#
# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list.




#Odd and Even
def odd_even():
    for num in range(1, 2001):
        if num % 2 == 0:
            print "Number is",num,". This is an even number."
        else: #if it isn't even, then the number is odd
            print "Number is",num,". This is an odd number."


#Multiply
def multiply(arr, mult):
    for i in range(0, len(arr)):
        arr[i] = arr[i]*mult #just set the index to the old index multiplied by the inputted multiplier
    print arr


#Hacker Challenge
def layered_multiples(arr):
    overall = [] #this is the overall area
    for i in arr:
        new_array = [] #this is the inner array
        for x in range(0,i): #this is putting in the right amount of 1s into the inner array
                new_array.append(1)
        overall.append(new_array)
    print overall
