#Making and Reading from Dictionaries

def info(name, age, bp, favelang): #this allows user to input whatever name, age, bp, and fave lang values
    details = {} #this is creating an empty dictionary which will be filled with the inputted info
    details["name"] = name
    details["age"] = age
    details["bp"] = bp
    details["favelang"] = favelang
    print "My name is", str(details["name"]) #now here we retrieve that info and print
    print "My age is", str(details["age"])
    print "My birthplace is", str(details["bp"])
    print "My favorite language is", str(details["favelang"])
