class Animals:
    def speak(self):
        print("This is an animal.")

class Pets(Animals):
    def pet_info(self):
        print("This is a pet.")

class Dog(Pets):
    def bark(self):
        print("Woof! Woof!")

# Example
dog = Dog()
dog.speak()      # From Animals
dog.pet_info()   # From Pets
dog.bark()       # From Dog
