#Product OOP Assignment

class Product(object):

    #Weight must be inputted in lbs; Currency is in US Dollars
    def __init__(self, price, item, weight, brand, cost):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale!"

    def sell(self):
        self.status = "Sold"
        return self

    #Tax is in decimals
    def add_tax(self, tax):
        self.price = self.price - (self.price * tax)
        return self

    def Return(self, reason, box):
        if reason == "defective":
            self.status = reason
            self.price = 0
        if box == "open":
            self.status = "Used"
            self.price = self.price - (self.price * 0.2)
        elif box == "closed":
            self.status = "For Sale!"
        return self

    def display_info(self):
        print "Product: %s" %(self.item)
        print "Price: $%s" %(self.price)
        print "Brand: %s" %(self.brand)
        print "Weight: %s lbs" %(self.weight)
        print "Cost: $%s" %(self.cost)
        print "Status: %s" %(self.status)

#Trial
product1 = Product(80, "Shoes", 0.2, "Nike", 20)
product1.display_info()
product1.add_tax(0.1)
product1.sell()
product1.display_info()
product1.Return("Wrong colour", "closed")
product1.display_info()
