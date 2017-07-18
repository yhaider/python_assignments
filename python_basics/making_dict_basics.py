# Assignment: Making Dictionaries
# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.


#Making Dictionaries

"""
Important: Any user with equal length arrays
should assume the first array will be the keys.
"""

def make_dict(arr1, arr2): #function with two inputted arrays
    if len(arr1) >= len(arr2): #this says that if arr1 is the longer one then those are keys. Also if they are the same, then the first inputted array is key
        combine_lists = zip(arr1,arr2) #the zip function allows us to make lists into tuples
        new_dict = dict(combine_lists)
        print new_dict
    else: #this says if arr2 is the longest, then it is used to be keys
        combine_lists = zip(arr2,arr1)
        new_dict = dict(combine_lists)
        print new_dict
