#8. The super() Function
#Assignment:
#Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
        print("Teacher constructor called")

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Create an object of Teacher
teacher1 = Teacher("Ms. Tehreem", "Mathematics")
teacher1.display()

