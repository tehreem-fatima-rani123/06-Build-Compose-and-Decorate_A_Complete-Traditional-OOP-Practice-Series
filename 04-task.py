#4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    # Class variable
    bank_name = "National Bank"

    def __init__(self, customer):
        self.customer = customer

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Customer: {self.customer}, Bank: {self.bank_name}")

# Create instances
cust1 = Bank("Ali")
cust2 = Bank("Tehreem")

# Show original bank name
cust1.show_details()
cust2.show_details()

# Change bank name using class method
Bank.change_bank_name("Global Trust Bank")

# Show updated bank name for all instances
cust1.show_details()
cust2.show_details()
