# Optional Assignment: Multiplication Table
# Create a program that prints a multiplication table in your console.



#Multiplication Table

def mult():
    print 'x 1 2 3 4 5 6 7 8 9 10 11 12' #this is the top
    for row in range(1, 13): #go to 13 because doesn't include 13 in for loop
        numbers  = '' #currently empty
        for column in range(0, 13): #this moves through the rows via columns
            if column is 0: #since it is the first row, this one is just the row numbers
                numbers += ' ' + str(row)
            else: #this requires multiplication
                numbers += ' ' + str(column * row)
        print numbers
