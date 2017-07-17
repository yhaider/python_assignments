#Checkerboard

def checker():
    for x in range(0,8): #you can change the range based on how big you want your board to be
        if x % 2 == 0: #randomly decided that if the number is even, it will emit this pattern
            print " * * * *"
        else: #if odd, this one
            print "* * * * "
#using even and odd to differentiate was the most intuitive since it is an alternating pattern like on the board
