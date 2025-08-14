#Practice Question 7
# File name to check
filename = "ques6.txt"  # Change this to your actual file name

# Open the file and search for "python"
with open(filename, "r") as file:
    lines = file.readlines()

found = False
for line_number, line in enumerate(lines, start=1):
    if "python" in line.lower():  # case-insensitive search
        print(f"'python' found at line {line_number}: {line.strip()}")
        found = True

if not found:
    print("'python' not found in the file.")
