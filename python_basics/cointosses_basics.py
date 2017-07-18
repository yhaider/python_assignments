# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!



#Coin Tosses

import random

def flip():
    print "Starting the program..." #this is to put the starting the program thing in the beginning and not with every loop
    heads = 0 #these two are to keep track
    tails = 0
    for turn in range(1, 5001): #the number of times wanted
        chance = random.random()
        if chance > 0.5:
            heads += 1
            print "Attempt #",turn,"Throwing a coin...It's a head!...Got",heads,"head(s) and",tails,"tail(s) so far."
        elif chance <= 0.5:
            tails += 1
            print "Attempt #",turn,"Throwing a coin...It's a tail!...Got",heads,"head(s) and",tails,"tail(s) so far."
    print "Ending the program. Thank you!"
