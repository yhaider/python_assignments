# Assignment: Stars
# Write the following functions.
#
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *
#
# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
#



#Stars Part I

def draw_stars(arr):
    for number in arr:
        if isinstance(number, int) == True: #need to be sure input is a number
            stars = ""
            for x in range(0, number):
                stars += "*"
            print stars
        else:
            print "Value is not an integer."


#Stars Part II

def draw_stars_2(arr):
    for item in arr:
        if isinstance(item, int) == True:
            stars = ""
            for x in range(0, item):
                stars += "*"
            print stars #above this, everything is the same as part one
        elif isinstance(item, str) == True:
            times = len(item)
            letter = item[0].lower() #this part takes the first character and makes it lowercase
            print letter * times #it multiplies it by the length of the item
        else:
            print "Value is not an integer or string."
