marks = {
    "Ahamd": 96,
    "Ali" : 90,
    "Haider": 80,
    0: "CMD"
}
print(marks, type(marks))
print(marks["Ahamd"])
print(marks.keys())

#updating the dict
marks.update({"Ahmad":99})
print(marks)

#
print(marks.get("Ahmad1"))  #will print none as key is not found
print(marks["Ahamd"])