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
