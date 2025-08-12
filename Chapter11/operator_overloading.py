#Operator Overloading in Pythion
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Operator overloading for +
    def __add__(self, other):
        # Add salaries of two employees
        return self.salary + other.salary

    # Operator overloading for >
    def __gt__(self, other):
        # Compare salaries
        return self.salary > other.salary

    def __str__(self):
        return f"Employee({self.name}, Salary: {self.salary})"


# ------------------------------
# Example Usage
# ------------------------------
emp1 = Employee("Ahmad", 500000)
emp2 = Employee("Ahsan", 600000)

# Using overloaded +
total_salary = emp1 + emp2
print(f"Total salary of {emp1.name} and {emp2.name} is {total_salary}")

# Using overloaded >
if emp1 > emp2:
    print(f"{emp1.name} has a higher salary.")
else:
    print(f"{emp2.name} has a higher salary.")
