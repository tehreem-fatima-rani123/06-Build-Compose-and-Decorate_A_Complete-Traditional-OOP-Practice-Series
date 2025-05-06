#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee Name:", self.name)

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference to existing Employee

    def show_details(self):
        print("Department:", self.department_name)
        self.employee.show()  # Using Employee's method

# Create an Employee object (independent)
emp = Employee("Tehreem")

# Department is created with a reference to the Employee object
dept = Department("IT", emp)

# Show details
dept.show_details()
