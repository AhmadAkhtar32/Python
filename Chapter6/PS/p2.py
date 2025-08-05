m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))


tm = (100)*(m1 + m2 + m3 )/300

if (tm>40 and m1>33 and m2>33 and m3>33):
    print("You are passed!", tm, "%")
else:
    print("You are Failed!", tm, "%")