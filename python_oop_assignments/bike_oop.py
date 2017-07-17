#Bike OOP Assignment

class bike(object):
    #Called init first since it is called every time there is a new instance
    def __init__(self,price, max_speed):
        self.price = price
        self.max = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Bike price is %s" %(self.price)
        print "Bike max speed is %s" %(self.max)
        print "Total miles travelled are %s" %(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        elif self.miles < 5:
            self.miles = 0
        #the above is so that we do not have negative miles, so if it is less than 5, the total goes to 0

#Trial run
my_bike = bike(100.00, 30)
my_bike.displayInfo()
my_bike.ride()
my_bike.ride()
my_bike.ride()
my_bike.ride()
my_bike.ride()
my_bike.reverse()
my_bike.reverse()
my_bike.reverse()
my_bike.displayInfo()
