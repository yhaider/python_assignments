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
