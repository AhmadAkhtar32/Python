import random

def check_winner(computer, user):
    if computer == user:
        return "It's a tie!"
    elif (computer == 's' and user == 'w') or \
         (computer == 'w' and user == 'g') or \
         (computer == 'g' and user == 's'):
        return "Computer wins!"
    else:
        return "You win!"

print("Welcome to Snake Water Gun Game!")
print("Choose: 's' for Snake, 'w' for Water, 'g' for Gun")

# Computer chooses randomly
options = ['s', 'w', 'g']
computer_choice = random.choice(options)

# User input
user_choice = input("Your choice (s/w/g): ").lower()

# Validate input
if user_choice not in options:
    print("Invalid input. Please choose 's', 'w', or 'g'.")
else:
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")
    print(check_winner(computer_choice, user_choice))
