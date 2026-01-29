import random
import string

def generate_password(total_length, num_letters, num_digits, num_specials):
    if num_letters + num_digits + num_specials != total_length:
        print("Error: The counts do not add up to the total length.")
        return None

    password_chars = []

    for _ in range(num_letters):
        password_chars.append(random.choice(string.ascii_letters))

    for _ in range(num_digits):
        password_chars.append(random.choice(string.digits))

    for _ in range(num_specials):
        password_chars.append(random.choice(string.punctuation))

    random.shuffle(password_chars)

    return ''.join(password_chars)


total_length = int(input("Enter total password length: "))
num_letters = int(input("Enter number of letters: "))
num_digits = int(input("Enter number of digits: "))
num_specials = int(input("Enter number of special characters: "))

password = generate_password(total_length, num_letters, num_digits, num_specials)

if password:
    print("Generated password:", password)
