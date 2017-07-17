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
