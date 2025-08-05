n1 = int(input("Enter Number1: "))
n2 = int(input("Enter Number2: "))
n3 = int(input("Enter Number3: "))
n4 = int(input("Enter Number4: "))

if (n1>2 and n1>n3 and n1>n4):
    print("The Greates Number is: ", n1)
elif (n2>n1 and n2>n3 and n2>n4):
    print("The Greates Number is: ", n2)
elif (n3>2 and n3>n1 and n3>n4):
    print("The Greates Number is: ", n3)
elif (n4>2 and n4>n3 and n4>n1):
    print("The Greates Number is: ", n4)