class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100


# Example
emp = Employee(50000, 10)
print(emp.salaryAfterIncrement)  # Getter

emp.salaryAfterIncrement = 60000  # Setter updates increment
print(emp.increment)
