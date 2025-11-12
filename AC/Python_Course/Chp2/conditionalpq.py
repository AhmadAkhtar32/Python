#WAP To check if a number entered by the user is odd or even
# WAP to check if a number entered by the user is odd, even, or zero

num0 = int(input("Enter The Number: "))

if num0 == 0:
    print("The Number Is Zero!")
elif num0 % 2 == 0:
    print("The Number Is Even!")
else:
    print("The Number Is Odd!")



# WAP to find the greatest of 3 numbers entered by the user

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)



# WAP to check if a number is a multiple of 7 or not

num = int(input("Enter a number: "))

if num % 7 == 0:
    print("The number is a multiple of 7!")
else:
    print("The number is not a multiple of 7!")

