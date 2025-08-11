import random  # Import random module

# Step 1: Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Step 2: Initialize variables
guess_count = 0
user_guess = None

print("🎯 Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Try to guess it!")

# Step 3: Loop until the correct guess
while user_guess != number_to_guess:
    guess_count += 1  # Increment attempts
    try:
        # Ask the user for input and convert to integer
        user_guess = int(input("Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue  # Skip to next iteration

    # Step 4: Compare guess with the number
    if user_guess > number_to_guess:
        print("📉 Lower number please!")
    elif user_guess < number_to_guess:
        print("📈 Higher number please!")
    else:
        print(f"✅ Congratulations! You guessed the number in {guess_count} attempts.")
