# Dictionary in Python
# Dictionaries are used to store data values in (key:value) pairs
# “key” : value
# They are unordered, mutable(changeable) & don’t allow duplicate keys

info = {
    "Name": ["Ahmad", "Ali", "Asad"],
    "Age": 23,
    "Education": "Graduate",
    "Cities": ("Lahore", "Isalamabad", "Sahiwal")
}
print(info)

# Tuple vs List vs Set vs Dictionary
# List: Ordered, indexed, mutable collection allowing duplicates.
# Tuple: Ordered, indexed, immutable collection allowing duplicates.
# Dictionary: Unordered key–value pairs, mutable, keys must be unique.
# Set: Unordered, mutable collection of unique elements only.


# Nested Dictionary
student = {
    "Name": "Ahmad",
    "Score": {
        "DSA": 90,
        "OOp": 85,
        "PF": 91
    }
}

print(student)
print(student.keys())
print(student.values())
print(student.items())
student.update({"City": "Islamabad"})   # Can add new value and also can update previous_one
print("After Update:", student)
