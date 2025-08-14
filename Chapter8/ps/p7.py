#Practice Question 7
# Function For Removing Word from List

def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["Ahmad", "Ahsan", "Ah", "Ahish"]

print(rem(l, "Ah"))