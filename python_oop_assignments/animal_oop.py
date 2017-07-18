# Assignment: Animal
# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.
#
# Objective
# The objective of this assignment is to help you understand inheritance. Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.
#
# Animal Class
# Attributes:
#
# • name
#
# • health
# Methods:
#
# • walk: decreases health by one
#
# • run: health decreases by five
#
# • display health: print to the terminal the animal's health.
# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.
#
# Dog Class
# • inherits everything from Animal
# Attributes:
#
# • default health of 150
# Methods:
#
# • pet: increases health by 5
# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
#
# Dragon Class
# • inherits everything from Animal
# Attributes:
#
# • default health of 170
# Methods:
#
# • fly: decreases health by 10
#
# • display health: prints health by calling the parent method and prints "I am a Dragon"
# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().





#Animal OOP Assignment

class Animal(object): #Overarching parent class
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health: %s" %(self.health)

class Dog(Animal): #Dog class specifically because only dogs can be pet and they have to have 150 health
    def __init__(self, name):
        super(Dog,self).__init__(self, name)
        self.health = 150
        return self
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal): #Dragon class specifically because only dragons can fly and they have to start with 170 health
    def __init__(self, name):
        super(Dragon,self).__init__(self, name)
        self.health = 170
        return self
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a dragon!"



#Trials
animal1 = Animal("Monty the cat", 100)
animal1.display_health()
animal1.walk()
animal1.run()
animal1.display_health()

dog1 = Dog("Fido")
dog1.display_health()
dog1.walk()
dog1.run()
dog1.pet()
dog1.display_health()

dragon1 = Dragon("Toothless")
dragon1.display_health()
dragon1.walk()
dragon1.run()
dragon1.fly()
dragon1.display_health()
