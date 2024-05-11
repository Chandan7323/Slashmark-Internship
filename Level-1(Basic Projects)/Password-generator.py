Secure Password Generator

This Python script generates strong, random passwords that meet security best practices.

Features:
*Generates multiple passwords at once (specify the number)
*Configurable password length (minimum 3 characters)
*Ensures passwords include:
   *Lowercase letters
   *Numbers (at least 1, randomly placed)
   *Uppercase letters (at least 1, randomly placed)

How to Use:
1.Clone or download the repository.
2.Open a terminal or command prompt and navigate to the directory containing the code (password_generator.py).
3.Run the script using python password_generator.py.
4.Enter the desired number of passwords to generate.
5.For each password, specify a length greater than or equal to 3.
6.The script will display the generated passwords, each containing lowercase letters, numbers, and an uppercase letter.



import random

def generate_password(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for l in length:
        password = ''.join(random.choice(alphabet) for _ in range(l))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)

    return passwords

def replace_with_number(password):
    for _ in range(random.randint(1, 2)):
        replace_index = random.randint(0, len(password) // 2 - 1)
        password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    for _ in range(random.randint(1, 2)):
        replace_index = random.randint(len(password) // 2, len(password) - 1)
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def get_password_lengths(num_passwords):
    print("Minimum length of password should be 3")
    return [max(int(input(f"Enter the length of Password #{i+1}: ")), 3) for i in range(num_passwords)]

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")
    password_lengths = get_password_lengths(num_passwords)
    passwords = generate_password(password_lengths)

    for i, password in enumerate(passwords):
        print(f"Password #{i+1}: {password}")

if __name__ == "__main__":
    main()
