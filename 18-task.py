#18. Property Decorators: @property, @setter, and @deleter
 #   Assignment:
 #   Create a class Product with a private attribute \_price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            print("Setting price...")
            self._price = value
        else:
            print("Price cannot be negative!")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create an object
item = Product(100)

# Access the price
print(item.price)

# Set a new price
item.price = 150

# Try setting a negative price
item.price = -50

# Delete the price
del item.price
