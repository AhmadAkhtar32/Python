# Define a class named Employee
class Employee:
    # __init__ is the constructor that runs automatically when a new object is created
    def __init__(self, name, salary):
        # 'self.name' and 'self.salary' are instance attributes
        self.name = name      # Store the 'name' passed during object creation
        self.salary = salary  # Store the 'salary' passed during object creation

    # Method to display employee details
    def getSalary(self):
        print(f"{self.name}'s salary is {self.salary}")

# Creating an object of Employee class
# When this line runs, __init__() is called automatically with:
#   self  -> the new object being created
#   name  -> "Ahsan"
#   salary -> 50000
ahsan = Employee("Ahsan", 50000)

# Accessing a method
ahsan.getSalary()   # Output: Ahsan's salary is 50000

# Creating another employee object
ahmad = Employee("Ahmad", 80000)
ahmad.getSalary()   # Output: Ahmad's salary is 80000
