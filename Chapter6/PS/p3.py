w1 = "buy now"
w2 = "open the link"
w3 = "come to telegram"
w4 = "subscribe this"

m = input("Enter your Comment: ")

if (w1 in m or w2 in m or w3 in m or w4 in m):
    print("This Message is a spam! Be aware!")

else: 
    print("This is not a spam!")