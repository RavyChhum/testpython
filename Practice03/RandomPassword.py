import random
import string

def generate_password(num_letters, num_symbols, num_numbers):
    # Define possible characters
    letters = string.ascii_letters
    symbols = string.punctuation
    numbers = string.digits

    # Create the password list with the required numbers of each character type
    password = [
        random.choice(letters) for _ in range(num_letters)
    ] + [
        random.choice(symbols) for _ in range(num_symbols)
    ] + [
        random.choice(numbers) for _ in range(num_numbers)
    ]

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Get user input for the number of each type of character
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

# Generate and print the password
password = generate_password(num_letters, num_symbols, num_numbers)
print("Generated password:", password)