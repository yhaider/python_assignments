# Assignment: Dictionary in, tuples out
# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value.

#Dictionary In, Tuples Out

def dict_tup(input_dict): #I made this so a user can put in whatever dictionary they want to
    info = [] #empty list to append to
    for key in input_dict:
        data_tuple = (key, input_dict[key]) #the data tuple that will be in each index of the list
        info.append(data_tuple) #append the data tuple into the list
    print info
