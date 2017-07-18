# Assignment: Call Center
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
#
# You will create two classes. One class should be Call, the other CallCenter.
#
# Call Class
# • Create your call class with an init method. Each instance of Call() should have:
# Attributes:
#
# • unique id
#
# • caller name
#
# • caller phone number
#
# • time of call
#
# • reason for call
# Methods:
#
# • display: that prints all Call attributes.
# CallCenter Class
# • Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
# Attributes:
#
# • calls: should be a list of call objects
#
# • queue size: should be the length of the call list
# Methods:
#
# • add: adds a new call to the end of the call list
#
# • remove: removes the call from the beginning of the list (index 0).
#
# • info: prints the name and phone number for each call in the queue as well as the length of the queue.
# You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
#
# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
#
# Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.


#Call Center OOP Assignment

from datetime import datetime

class Call(object):
    def __init__(self, name, number, reason):
        self.id_no = id(self)
        self.time = datetime.now()
        self.call = [self.id_no,
                    name,
                    number,
                    self.time,
                    reason]

#Display prints the call's information in a list
    def display(self):
        print self.call



class CallCenter(Call):
    def __init__(self):
        self.call_list = []
        self.queue_size = 0

#add() adds a new call into the call list
    def add(self, name, number, reason):
        super(CallCenter, self).__init__(name, number, reason)
        self.call_list.append(self.call)
        self.queue_size += 1
        return self

#remove() gets rid of the first call in the list
    def remove(self):
        self.call_list.pop(0)
        self.queue_size -= 1
        return self

#Remove specific allows for a specific call to be removed based on its number
    def remove_specific(self, phone_number):
        for i in range(self.queue_size - 1):
            if self.call_list[i][2] == phone_number:
                self.call_list.pop(i)
                self.queue_size -= 1

#Info allows prints name and number for each call in the queue and the queue size
    def info(self):
        for indiv_call in self.call_list:
            print indiv_call[1], indiv_call[2]
        print self.queue_size

#Sort Queue sorts the queue by time of call
    def sort_queue(self):
        self.call_list = sorted(self.call_list, key=lambda x:x[3])

#Trial
call1 = Call("Sam", 18005882300,"email not working")
call2 = Call("Bob", 2405678910,"server issue")
call3 = Call("Joe", 3016762355,"website hacked")
call4 = Call("Tom", 9174578297,"computer virus")

call2.display()

#Testing out Call Center
callcenter = CallCenter()
callcenter.add("Sam", 18005882300,"email not working")
callcenter.add("Bob", 2405678910,"server issue")
callcenter.add("Joe", 3016762355,"website hacked")
callcenter.add("Tom", 9174578297,"computer virus")
callcenter.info()
#Ran info above to see it before we used other methods to manipulate the call list
callcenter.remove()
callcenter.remove_specific(3016762355)
callcenter.sort_queue()
callcenter.info()
