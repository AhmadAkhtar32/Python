# ------------------------------
# Grandparent Class
# ------------------------------
class Animal:
    def __init__(self, species):
        self.species = species

    def eat(self):
        print(f"{self.species} is eating.")

# ------------------------------
# Parent Class (inherits from Animal)
# ------------------------------
class Mammal(Animal):
    def __init__(self, species, has_fur):
        # Call the grandparent constructor using super()
        super().__init__(species)
        self.has_fur = has_fur

    def walk(self):
        print(f"{self.species} is walking on land.")

# ------------------------------
# Child Class (inherits from Mammal)
# ------------------------------
class Dog(Mammal):
    def __init__(self, breed, has_fur=True):
        # Call the parent constructor
        super().__init__("Dog", has_fur)
        self.breed = breed

    def bark(self):
        print(f"{self.breed} is barking! Woof woof!")

# ------------------------------
# Example Usage
# ------------------------------
my_dog = Dog("German Shepherd")

# Methods from Grandparent
my_dog.eat()

# Methods from Parent
my_dog.walk()

# Methods from Child
my_dog.bark()

# Attributes from all levels
print(f"Species: {my_dog.species}, Breed: {my_dog.breed}, Has Fur: {my_dog.has_fur}")
