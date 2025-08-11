class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    # Getter (property)
    @property
    def salary(self):
        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value


# ------------------------------
# Usage
# ------------------------------
emp = Employee("Ahsan", 70000)

# Access like an attribute (calls getter)
print(emp.salary)

# Assign like an attribute (calls setter)
emp.salary = 80000
print(emp.salary)

# emp.salary = -5000  # Raises ValueError
