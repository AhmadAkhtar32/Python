#self parameter in python
class Car:
    name = "Civic"
    status = "Available"
    Company = "Honda"
    Price = "9000000"

    def getinfo(self):
        print(f"The Company is: {self.Company}. The Price is: {self.Price}")

vehicle = Car()
print(Car.name, Car.Company, Car.Price, Car.status)

Car.getinfo(vehicle)
