#Practice Question 3
class Test:
    a = 5  # Class attribute

obj = Test()
print("Before change:", Test.a)  # Output: 5

# Changing via object
obj.a = 0
print("After object change:", obj.a)  # Output: 0 (only for this object)
print("Class attribute still:", Test.a)  # Output: 5 (unchanged)
