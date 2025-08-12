#Class Methids in Python
class Employee:
    # Class attribute (shared by all objects)
    company_name = "TechCorp"

    def __init__(self, name, salary):
        # Instance attributes (unique to each object)
        self.name = name
        self.salary = salary

    # Class method to change class attribute
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company
        print(f"Company name changed to {cls.company_name}")

    # Class method as a factory method (creating object from string)
    @classmethod
    def from_string(cls, emp_str):
        # Suppose emp_str = "Name-Salary"
        name, salary = emp_str.split("-")
        return cls(name, int(salary))

    # Instance method for showing details
    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company_name}")


# ------------------------------
# Example Usage
# ------------------------------

# Creating object normally
emp1 = Employee("Ahmad", 400000)
emp1.show_details()

# Creating object using a class method (factory method)
emp2 = Employee.from_string("Ahsan-500000")
emp2.show_details()

# Changing company name for all employees
Employee.change_company("CodeMasters")

# Now both emp1 and emp2 have updated company name
emp1.show_details()
emp2.show_details()
