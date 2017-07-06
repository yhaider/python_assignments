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
