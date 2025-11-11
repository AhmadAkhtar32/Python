#String is data type that stores a sequence of characters.
#Strings in python are surrounded by either single quotation marks, or double quotation marks.

#'hello' is the same as "hello". This is a string

#You can display a string literal with the print() function:

#Concatenation
print("Hello"  +  "Developers")

str1 = "This is the First String"

print(str1)

#Assign String to a Variable
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

#Example
#a = "Hello"
#print(a)


#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

#Example
#You can use three double quotes:

#a = """Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)


#Escapesequence Characters ! 

str2 = "This is the use of escape sequence chrs. \nWe are using it to move text to next line"
str3 = "This is the use of escape sequence chrs. \t We are using it to give big space line"
print(str2)
print(str3)


# The Process of joining two strings in Python is known as "Concatenation" Nd we use "+" for this

str4 = "This is string 4 \n"
str5 = "This is string 5."
str6 = (str4+str5)
print(str6)

#printing the length of string
print(len(str6))
final_str = (str5 + " " + str3)
print(final_str)

#Accessing a chr in a String using indexing
a = str5[3]
print(a)
print(str4[2])

# Slicing is used for Accessing the parts of String !
# string_name[starting index : ending index]
print(str4[0:6])
print(str4[:6])
print(str4[6:])

# Negative index while doing slicing in Python 
str_new = "Islamabad"
print(str_new[-4: -1])