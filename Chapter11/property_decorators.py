class Employee:
    def __init__(self, name, salary):
        self._name = name       # Convention: _variable means "private" (internal use)
        self._salary = salary

    # Getter (read)
    @property
    def salary(self):
        print("Getting salary...")
        return self._salary

    # Setter (write)
    @salary.setter
    def salary(self, value):
        print("Setting salary...")
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

    # Deleter (delete)
    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self._salary


# ------------------------------
# Example Usage
# ------------------------------
emp = Employee("Ahmad", 50000)

# Accessing salary like an attribute (calls the getter)
print(emp.salary)  

# Changing salary (calls the setter)
emp.salary = 60000
print(emp.salary)

# Trying to set negative salary (will raise error)
# emp.salary = -1000  # Uncomment to test error

# Deleting salary (calls the deleter)
del emp.salary
