#5. Static Variables and Static Methods
#Assignment:
#Create a class MathUtils with a static method add(a, b) that #returns the sum. No class or instance variables should be used.



class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

# Example usage
result = MathUtils.add(10, 15)
print("Sum:", result)
