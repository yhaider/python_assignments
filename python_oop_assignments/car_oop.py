# Assignment: Car
# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
#
# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.




#Car OOP Assignment

class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000: #Price of car impacts tax so this if and elif statement addresses that
            self.tax = 0.15
        elif self.price <= 10000:
            self.tax = 0.12

    def displayall(self):
        print "Price: $%s" %(self.price)
        print "Speed: %s mph" %(self.speed)
        print "Fuel: %s" %(self.fuel)
        print "Mileage: %s mpg" %(self.mileage)
        print "Tax: %s" %(self.tax)
        return self

#Trial
car1 = Car(2000, 35, "Full", 15)
car1.displayall()

car2 = Car(11000, 45, "Not Full", 100)
car2.displayall()

car3 = Car(5000, 5, "Full", 95)
car3.displayall()
