# Loops are used to repeat instructions
# Python has two primitive loop commands:
# while loops
# for loops

# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

count = 1
while count <=5 :
    print("Hello")
    count += 1

# Print numbers from 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1



# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# Example
# Exit the loop when i is 3:

p = 1
while p < 6:
  print(p)
  if p == 3:
    break
  p += 1