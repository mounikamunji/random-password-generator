# random-password-generator
Overview
This is a simple Python console application that generates a random password based on the user-specified length. The generated password can include uppercase letters, lowercase letters, digits, and special characters.

Features
Generate a random password of any length

Password includes letters (both uppercase and lowercase), digits, and special characters

Easy to use with simple console input

Requirements
Python 3.x

How to Run
Save the script (password_generator.py) on your computer.

Open a terminal or command prompt.

Navigate to the folder where the script is saved.

Run the program with the command:

nginx
Copy
Edit
python password_generator.py
When prompted, enter the desired password length.

The program will output the generated password.

Example Usage
pgsql
Copy
Edit
Enter password length: 12
Generated Password: f!9D3z@TqL2$
Code Snippet
python
Copy
Edit
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
License
This project is free and open source.

