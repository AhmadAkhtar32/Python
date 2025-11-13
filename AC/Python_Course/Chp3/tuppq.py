#WAP to count the number of students with the “A” grade in the tuple
# Given tuple
grades = ("C", "D", "A", "A", "B", "B", "A")

# Count number of "A" grades
count_A = grades.count("A")

print("Number of students with A grade:", count_A)


#Store the tuple values in a list & sort them from "A" to "D"
grades = ("C", "D", "A", "A", "B", "B", "A")

# Convert tuple → list
grade_list = list(grades)

# Sort list alphabetically
grade_list.sort()

print("Sorted grades (A to D):", grade_list)
