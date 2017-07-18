# Assignment: String and List Practice
# Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:
#
# • .find()
#
# • .replace()
#
# • min()
#
# • max()
#
# • .sort()
#
# • len()
#
# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
#
# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
#
# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
#
# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!







#Find and Replace
def findandreplace():
    string = "It's thanksgiving day. It's my birthday, too!"
    dayposition = string.find("day")
    print dayposition
    newstr = string.replace("day", "month")
    print newstr

#Min and Max
def maxandmin():
    list = [2, 54, -2, 7, 12, 98]
    print min(list)
    print max(list)

#First and Last
def firstandlast():
    lst = ["hello", 2, 54, -2, 7, 12, 98, "world!"]
    print lst[0]
    print lst[len(lst) - 1]
    newlst = [lst[0], lst[len(lst) - 1]]

#New list
def newlist():
    x = [19,2,54,-2,7,12,98,32,10,-3,6]
    x.sort()
    inside = x[:len(x)/2]
    final = x[len(x)/2:]
    final.insert(0,inside)
    print final
