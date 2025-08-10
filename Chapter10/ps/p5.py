class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The train {self.name} has {self.seats} seats available.")

    def getFareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Seat number: {self.seats}")
            self.seats -= 1
        else:
            print("Sorry, the train is full.")

# Example usage
train1 = Train("Rajdhani Express", 1500, 2)
train1.getStatus()
train1.bookTicket()
train1.getStatus()
train1.getFareInfo()
