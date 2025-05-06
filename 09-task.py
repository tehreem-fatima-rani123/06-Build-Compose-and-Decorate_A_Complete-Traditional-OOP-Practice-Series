#9. Abstract Classes and Methods
#Assignment:
#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass  # Abstract method has no implementation

# Concrete subclass
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Instantiate Rectangle
rect = Rectangle(5, 4)
print("Area of rectangle:", rect.area())
