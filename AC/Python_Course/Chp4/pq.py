# ✅ Practice Question 1
# Store the following word meanings in a Python dictionary:
# table : “a piece of furniture”, “list of facts & figures”
# cat : “a small animal”

# Word meanings dictionary
word_meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": ["a small animal"]
}

print(word_meanings)


# ✅ Practice Question 2
# **You are given a list of subjects for students.
# Assume one classroom is required for one subject.
# How many classrooms are needed?**

subjects = [
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "C"
]

# Using a set to get unique subjects
unique_subjects = set(subjects)
print("Unique Subjects:", unique_subjects)
print("Total Classrooms Needed:", len(unique_subjects))


# Problem 3: Dictionary Practice
# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add entries one by one. Use the subject name as the key and marks as the value.

# Start with an empty dictionary
marks = {}

# Get input for 3 subjects
for i in range(3):
    subject = input("Enter subject name: ")
    mark = float(input(f"Enter marks for {subject}: "))
    marks[subject] = mark

# Display the dictionary
print("\nSubject-wise marks:")
print(marks)


# Problem 4: Set with Integer and Float
# Figure out a way to store 9 and 9.0 as separate values in a set (hint: use built-in data types).
# Convert one value to string to make them distinct
my_set = {9, "9.0"}
print(my_set)  # Output: {9, '9.0'}

# Or use complex numbers
my_set = {9, 9.0+0j}
print(my_set)  # Output: {9, (9+0j)}

# Or use tuples
my_set = {9, (9.0,)}
print(my_set)  # Output: {9, (9.0,)}