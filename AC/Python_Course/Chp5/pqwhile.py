# Print Numbers from 1 To 100

i = 1
while i<=100:
    print(i)
    i +=1


# Print Numbers from 100 To 1

j = 100
while j>=1:
    print(j)
    j -=1

# print the multiplication of table for a number n

n = int(input("Enter a number: "))
k = 1

while k <= 10:
    print(n, "x", k, "=", n * k)
    k += 1

#Print all elements of the list using a while loop
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l = 0
while l < len(numbers):
    print(numbers[l])
    l += 1

#Search for a number x in the list using a while loop
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

y = int(input("Enter number to search: "))

m = 0
found = False

while m < len(numbers):
    if numbers[m] == y:
        found = True
        break
    m += 1

if found:
    print(y, "is present in the list.")
else:
    print(y, "is NOT present in the list.")


# Continue: terminates execution in the current iteration & continues execution of loop with the next iteration
