#Names Part I

def students():
    students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    for student in students:
         print student["first_name"], student["last_name"] #This simply prints first and last name for each dictionary item


#Names Part II
def stud_inst():
    users = {
    'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ],
    'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
     ]
     }
    number = 0
    for title in users: #This part prints the title of the people in the list
         print title
         for individual in users[title]: #Now here are individuals
             number += 1
             first_name = individual['first_name'].upper()
             last_name = individual['last_name'].upper()
             char = len(individual['first_name']) + len(individual['last_name'])
             print "%s - %s %s - %s" %(number, first_name, last_name, char)
#By setting the variables earlier and using %s, we can avoid having to concatenate strings to include the dashes
