# Python program to read a file and search a word in it
f = open("Chapter9/f.txt")
content = f.read()
if("Twinkle " in content):
    print("Twinkle is Present In File: f.txt")

else:
    print("Twinkle is not Present!")

f.close()