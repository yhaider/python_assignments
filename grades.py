#Scores and Grades

import random

def grades():
    for i in range(1, 11):
        score = random.randint(60, 100) #this limits the range where random integers can be chosen from
        if 60 <= score < 70:
            print "Score:",score,"Your grade is D."
        if 70 <= score < 80:
            print "Score:",score,"Your grade is C."
        if 80 <= score < 90:
            print "Score:", score, "Your grade is B."
        if 90 <= score <= 100:
            print "Score:", score, "Your grade is A."
