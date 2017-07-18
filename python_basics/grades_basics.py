# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A




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
