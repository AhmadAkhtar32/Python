#Without Warlus Operator
# line = input("Enter: ")
# while line != "quit":
#     print(f"You typed: {line}")
#     line = input("Enter: ")


# With Warlus Operator
while (line := input("Enter: ")) != "quit":
    print(f"You typed: {line}")

