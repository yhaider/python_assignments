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
