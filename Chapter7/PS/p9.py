n = int(input("Enter The Number: "))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*" * n)           # Print full stars in first and last rows
    else:
        print("*" + " " * (n-2) + "*")  # Print hollow rows
