#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

a = 33
b = 33
if a>b :
    print("A is greater than B")     #indentation before print word (tab/4spaces)
elif a ==b:
    print("A is equal to B")


#If checks the condition for always , while elif only checks next if condition falls true
num = int(input("Enter the Number: "))

if num > 10:
    print("Entered Number Is Greater Than 10!")
elif num < 10:
    print("Entered Number Is Less Than 10!")
else:
    print("Entered Number Is Equal To 10!")


marks = int(input("Enter The Marks: "))
if marks>=90:
    print("A+ Grade")
elif marks>=80:
    print("A Grade")
elif marks>= 70:
    print("B Grade")
elif marks>= 60:
    print("C Grade")
elif marks>= 50:
    print("D Grade")
else:
    print("Fail")
