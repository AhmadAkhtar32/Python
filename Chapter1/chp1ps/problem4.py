import os

# Specify the directory path (you can change this to any valid path)
directory_path = "."

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
