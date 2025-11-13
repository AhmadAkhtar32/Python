# Lists in Python
# A built-in data type that stores set of values
# marks = [87, 64, 33, 95, 76]
# It can store elements of different types (integer, float, string, etc.)

marks = ["Ahmad Rao", 12.34 , 23, 66.25 , True , 34]
print(marks)
print(marks[0])      # printing a specific value in List

#Strings are immutable(That can't be changed) in Python
#Lists are mutable(That can be changed) in Python

# Slicing is also possible in Lists

slc = [12, 23, 45 ,23 ,23 , 44,43]
print(slc)
print(slc[0:4])
print(slc[1:])
print(slc[-5:-2])



# Some Methods used in Lists
list1 = [2, 3, 4]
print("Original List:", list1)
list1.append(5)                     # Adds one element at the end
print("After append(5):", list1)
list1.sort()                        # Sorts the list in ascending order
print("After sort():", list1)
list1.sort(reverse=True)            # Sorts the list in descending order
print("After sort(reverse=True):", list1)
list1.reverse()                     # Reverses the list order
print("After reverse():", list1)
list1.insert(0 , 6)                 # inserting an element at some index in List
print("New List After Inserting: ", list1)