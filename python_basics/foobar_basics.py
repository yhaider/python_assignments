# Optional Assignment: Foo and Bar
# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
#
# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".


#Foobar

for i in (100, 100001): #overall range
    def perfect(i): #finding out the perfect numbers
        for y in range(1,i):
            if y*y == i:
                return True
                break
    def prime(i): #finding prime numbers
        for z in range(2, i):
            if i % z == 0:
                return False
                break
        else:
            return True
    if perfect(i) == True:
        print "Bar"
    elif prime(i) == True:
        print "Foo"
    else:
        print "FooBar"
