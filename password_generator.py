# Import the tools we need
import string
import random


# Function that generates a password of a given length
# "length" is how many characters the password should have
def generate_password(length):
    # Create a "bag" of characters: letters (a-z, A-Z) and digits (0-9)
    characters = string.ascii_letters + string.digits

    # Start with an empty password (an empty string)
    password = ""

    # Repeat "length" times
    for i in range(length):
        # Pick one random character from the bag
        char = random.choice(characters)

        # Add that character to the password
        password = password + char

    # After the loop, the password is ready
    return password


# This part runs only when you run the file directly (like: python3 password_generator.py)
if __name__ == "__main__":
    # Print a title so the user knows what the program does
    print("=== Password Generator ===")

    # Ask the user how long the password should be
    # Convert the answer from text to a number
    length = int(input("Password length: "))

    # Call the function to generate a password
    password = generate_password(length)

    # Show the result
    print("Generated password:", password)
