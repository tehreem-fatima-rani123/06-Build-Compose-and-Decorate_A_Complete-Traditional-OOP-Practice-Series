#3. Public Variables and Methods
#Assignment:
#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand  # public attribute

    # Public method
    def start(self):
        print(f"{self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Brand:", my_car.brand)

# Call public method
my_car.start()
