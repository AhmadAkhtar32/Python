#Practice Question
import os


# Step 1: Create a folder for the tables
folder_name = "Multiplication_Tables"
os.makedirs(folder_name, exist_ok=True)  # Create folder if not already present

# Step 2: Generate multiplication tables from 2 to 20
for num in range(2, 20 + 1):  # Loop from 2 to 20
    file_path = os.path.join(folder_name, f"table_{num}.txt")  # File name
    
    with open(file_path, "w") as file:
        file.write(f"Multiplication Table of {num}\n")
        file.write("=" * 30 + "\n")
        
        for i in range(1, 11):  # Table from 1 to 10
            line = f"{num} x {i} = {num * i}\n"
            file.write(line)

print(f"All tables have been saved in '{folder_name}' folder.")
