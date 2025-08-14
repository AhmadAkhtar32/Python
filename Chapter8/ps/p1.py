#Practice Question 1
a = int(input("Enter The Number: "))
b = int(input("Enter The Number: "))
c = int(input("Enter The Number: "))

def grt():
    if(a>b and a>c):
        print(f"The Greatest Number is: {a}")
    elif(b>a and b>c):
        print(f"The Greatest Number is: {b}")
    elif(c>b and c>a):
        print(f"The Greatest Number is: {c}")

grt()