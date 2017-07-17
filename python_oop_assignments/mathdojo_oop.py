#Math Dojo OOP Assignment

class MathDojo(object):
    def __init__(self, start):
        self.start = start
    def add(self, *addends):
        for i in addends:
            if isinstance(i, list): #This allows for lists to be inputted
                for num in i:
                    self.start += num
            elif isinstance(i, tuple): #This allows for tuples to be added
                for num in i:
                    self.start += num
            else: #This is for integers
                self.start += i
        return self
    def subtract(self,*subtrahends): #Same logic as above applied to this function
        for i in subtrahends:
            if isinstance(i,list):
                for num in i:
                    self.start -= num
            elif isinstance(i,tuple):
                for num in i:
                    self.start -= num
            else:
                self.start -= i
        return self
    def result(self):
        print self.start

#Trial
md = MathDojo(2)
md.add((2, 3)).subtract(5).result()
