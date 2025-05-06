#7. Access Modifiers: Public, Private, and Protected
#Assignment:
#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected (convention)
        self.__ssn = ssn          # Private

# Create an object
emp = Employee("Ali", 50000, "123-45-6789")

# Accessing public variable
print("Public (name):", emp.name)        # ✅ Accessible

# Accessing protected variable
print("Protected (_salary):", emp._salary)  # ⚠️ Accessible but discouraged (by convention)

# Accessing private variable directly (will cause error)
try:
    print("Private (__ssn):", emp.__ssn)     # ❌ Will raise AttributeError
except AttributeError:
    print("Private (__ssn): Cannot access directly!")

# Accessing private variable using name mangling (not recommended in practice)
print("Private (__ssn) via name mangling:", emp._Employee__ssn)  # ✅ Possible but discouraged

