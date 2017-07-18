# Optional Assignment: Store
# Now, let's build a store to contain our products by making a store class and putting our products into an array.
#
# Store class:
# Attributes:
#
# • products: an array of products objects
#
# • location: store address
#
# • owner: store owner's name
# Methods:
#
# • add_product: add a product to the store's product list
#
# • remove_product: should remove a product according to the product name
#
# • inventory: print relevant information about each product in the store
# You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.


#Optional Assignment: Store OOP

class Store(object):

    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, new_item):
        self.products.append(new_item)
        return self

    def inventory(self):
        print "INVENTORY"
        count = 1
        for i in range (0, len(self.products)):
            print "%s.) %s" %(count, self.products[i])
            count += 1 #Numbers the products as they are printed
    def remove_product(self, getridof):
        self.products.remove(getridof)
        return self

    def relay_info(self):
#This wasn't a part of the assignment, but I wanted a method that used the location and owner attributes, so I created it
        itemstr = ""
        for i in range(0, len(self.products)):
            if i == len(self.products) - 1:
                itemstr += "%s." %(self.products[i])
            else:
                itemstr += "%s, " %(self.products[i])
        print "This store is located at %s and owned by %s. It sells %s" %(self.location, self.owner, itemstr)


#Trial
store1 = Store(["Bananas", "Carrots", "Apples", "Berries", "Onions"], "123 Grocery Street", "Yasmeen")
store1.relay_info()
store1.add_product("Pineapples")
store1.remove_product("Berries")
store1.inventory()
