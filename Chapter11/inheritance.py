# inheritance In Python
# Parent Class
# ------------------------------
class Vehicle:
    def __init__(self, brand, model):
        # Constructor for initializing attributes
        self.brand = brand
        self.model = model

    def start_engine(self):
        # Method for starting the vehicle
        print(f"{self.brand} {self.model} engine started!")

    def stop_engine(self):
        # Method for stopping the vehicle
        print(f"{self.brand} {self.model} engine stopped!")


# ------------------------------
# Child Class (Inheriting from Vehicle)
# ------------------------------
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # Use 'super()' to call the parent class constructor
        super().__init__(brand, model)
        self.doors = doors  # Child's own attribute

    def open_trunk(self):
        # Child-specific method
        print(f"{self.brand} {self.model} trunk is now open.")

    # Overriding a method from parent class
    def start_engine(self):
        print(f"Car {self.brand} {self.model} is roaring to life!")  # Modified behavior


# ------------------------------
# Child Class (Inheriting from Vehicle)
# ------------------------------
class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def pop_wheelie(self):
        print(f"{self.brand} {self.model} pops a wheelie!")


# ------------------------------
# Example Usage
# ------------------------------

# Creating a Car object
car1 = Car("Toyota", "Corolla", 4)
car1.start_engine()  # Overridden method in Car class
car1.open_trunk()
car1.stop_engine()   # Inherited method from Vehicle

print()  # Just for spacing

# Creating a Bike object
bike1 = Bike("Yamaha", "MT-15", "Sports")
bike1.start_engine() # Inherited method from Vehicle
bike1.pop_wheelie()
bike1.stop_engine()  # Inherited method from Vehicle
