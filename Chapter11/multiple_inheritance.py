# Multiple Inherotance 
# Parent Class 1
# ------------------------------
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start_engine(self):
        print(f"Engine started with {self.horsepower} horsepower.")

# ------------------------------
# Parent Class 2
# ------------------------------
class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def rotate_wheels(self):
        print(f"{self.wheel_count} wheels are rotating smoothly.")

# ------------------------------
# Child Class (Multiple Inheritance)
# ------------------------------
class Car(Engine, Wheels):
    def __init__(self, brand, horsepower, wheel_count):
        # We need to call both parent constructors manually
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, wheel_count)
        self.brand = brand

    def show_details(self):
        print(f"{self.brand} car with {self.horsepower} HP and {self.wheel_count} wheels.")

# ------------------------------
# Example Usage
# ------------------------------
my_car = Car("BMW", 300, 4)

my_car.show_details()   # Method from child
my_car.start_engine()   # Inherited from Engine
my_car.rotate_wheels()  # Inherited from Wheels
