# Import the tools we need
import string
import random


# Function for Easy: only lowercase letters
def generate_password_easy(length):
    characters = string.ascii_lowercase
    password = ""
    for i in range(length):
        char = random.choice(characters)
        password = password + char
    return password


# Function for Medium: lowercase + uppercase + numbers
def generate_password_medium(length):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        char = random.choice(characters)
        password = password + char
    return password


# Function for Strong: add symbols
def generate_password_strong(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    for i in range(length):
        char = random.choice(characters)
        password = password + char
    return password


# Function to read and display all saved passwords
def show_saved_passwords():
    print("\n=== Saved Passwords ===")

    # Try to open the file and read all lines
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No passwords saved yet.")
        else:
            for line in lines:
                print(line.strip())  # .strip() removes the extra newline
    except FileNotFoundError:
        print("No passwords file found. You haven't saved any passwords yet.")


# This part runs only when you run the file directly
if __name__ == "__main__":
    # First show all saved passwords
    show_saved_passwords()

    print("\n=== Password Generator with Menu ===")
    print("1. Easy: only lowercase letters")
    print("2. Medium: lowercase + uppercase + numbers")
    print("3. Strong: all of the above plus symbols (!@#$%^&*)")
    print("4. Exit without generating a new password")

    # Ask the user which option they want
    choice = input("Choose strength (1, 2, 3) or 4 to exit: ")

    if choice == "4":
        print("Bye!")
        exit()

    # Ask the user how long the password should be
    length = int(input("Password length: "))

    # Ask for a label (like "Gmail", "Netflix", "School")
    label = input("Label for this password (e.g., Gmail): ").strip()

    # Decide what kind of password to make
    if choice == "1":
        password = generate_password_easy(length)
        level = "easy"
    elif choice == "2":
        password = generate_password_medium(length)
        level = "medium"
    elif choice == "3":
        password = generate_password_strong(length)
        level = "strong"
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        exit()

    # Print the generated password
    print("Generated password ({0}): {1}".format(level, password))

    # Save the password + label + level + length to a file
    with open("passwords.txt", "a") as file:
        file.write("Label: {0}, Level: {1}, Length: {2}, Password: {3}\n".format(label, level, length, password))

    print("Password saved to passwords.txt")
