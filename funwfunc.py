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
