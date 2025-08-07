#Functions with default arguments
def hey(name, ending="Thank You !"):
    print(f"Greetings, {name}")
    print(ending)

hey("Ahmad")  #will call default value for ending
hey("Ahsan ", "Thanks")  # will take new value for ending