#2. Using cls
#Assignment:
#Create a class Counter that keeps #track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    # Class variable to keep count of objects
    count = 0

    def __init__(self):
        # Increment count when a new object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Use cls to access class variable
        print("Number of objects created:", cls.count)

# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Displaying the count
Counter.show_count()