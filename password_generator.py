import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Password Generator ===")
    length = int(input("Password length: "))
    password = generate_password(length)
    print("Generated password:", password)
