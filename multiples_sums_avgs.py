#Multiples Part I
def oddnum():
    for x in range(1, 1001, 2): #this part of the function looks at x in the range of 1 to 1001 and adds 2 each time to get odd
        print x #then it prints each number

#Multiples Part II
def fives():
    for y in range (5, 1000000, 5): #this looks at the numbers between 5 and 1000000 adding 5 each time
        print y #then it prints each one

#Sum List
def sumlist():
    a = [1, 2, 5, 10, 255, 3] #Here we have the list
    sum = 0 #This is an empty variable that will be used to make the sum
    for y in range(0, len(a)): #Using a for loop so this function can be applicable to any list, like a is here
        sum += a[y] #This adds the number in a[y] to the sum
    print sum

#Average list
def avg():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for y in range(0, len(a)):
        sum += a[y] #Up till here literally copied the above function since we need the sum of the array to find the Average
    avg = sum/len(a) #Basic formula to find average, dividing by the total number of numbers which is array length
    print avg
