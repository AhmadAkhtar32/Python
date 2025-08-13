#Practice Question 1
class Programmer:
    company = "Microsoft"  # Class attribute (same for all programmers)

    def __init__(self, name, product):
        self.name = name        # Instance attribute
        self.product = product  # Instance attribute

# Creating objects
p1 = Programmer("Sara", "Office 365")
p2 = Programmer("Ahmad", "Windows 11")

# Display info
print(f"{p1.name} works at {p1.company} on {p1.product}")
print(f"{p2.name} works at {p2.company} on {p2.product}")
