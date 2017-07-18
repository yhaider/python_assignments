# Assignment: Bike
# Create a new class called Bike with the following properties/attributes:
#
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
#
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
#
# Add the following functions to this class:
#
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
#
# What would you do to prevent the instance from having negative miles?
#
# Which methods can return self in order to allow chaining methods?




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
