class Car:
    status= "Available"
    Company = "Honda"
    Price = "9000000"

vehicle = Car()
Car.name = "Civic"
print(Car.name, Car.Company, Car.Price, Car.status)

vehicle = Car()
Car.name = "Toyota"
print(Car.name, Car.Company, Car.Price, Car.status)

# Now here Car.name is Object Attribute while Car.status,company,price are Class Attributes ! 