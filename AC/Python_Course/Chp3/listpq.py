#WAP to ask the user to enter names of their 3 favourite movies & store them in a list
movies = []

# taking 3 movie names from the user
movie1 = input("Enter your 1st favourite movie: ")
movie2 = input("Enter your 2nd favourite movie: ")
movie3 = input("Enter your 3rd favourite movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print("Your favourite movies list:", movies)


# WAP to check if a list contains a palindrome of elements
# WAP to check if a list is a palindrome

list1 = [1, 2, 3, 2, 1]     # you can take input also
list2 = list1.copy()        # making a copy

list2.reverse()             # reversing copy of list

if list1 == list2:
    print("The list is a palindrome!")
else:
    print("The list is NOT a palindrome!")
