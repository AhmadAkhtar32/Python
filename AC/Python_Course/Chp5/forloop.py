# For Loops: 
# For loops are generally used for sequential traversal ! 

nums = [1,2,3,4,5]

for val in nums:
    print(val)


# A complex example of For loop In Python
sentences = [
    "Data Science is fun!",
    "Python is great for Data Analysis.",
    "Science and Python go hand in hand."
]

word_count = {}

for sentence in sentences:
    # Remove punctuation
    cleaned = ""
    for ch in sentence:
        if ch.isalnum() or ch == " ":
            cleaned += ch
    
    # Split into words
    words = cleaned.lower().split()
    
    # Count frequency of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
