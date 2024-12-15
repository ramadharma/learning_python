import random

# Lowercase Alphabets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']

print("Welcome to PyPassword Generator!")

in_letters = int(input("How many letters should you like in your password?\n"))
in_numbers = int(input("How many numbers should you like?\n"))
in_symbols = int(input("How many symbols should you like?\n"))

# Easy code 
password = ""
for char in range(0, in_letters):
    password += random.choice(letters)

for char in range(0, in_numbers):
    password += random.choice(numbers)

for char in range(0, in_symbols):
    password += random.choice(symbols)

print(password)

# Hard code 
password_list = []
for char in range(0, in_letters):
    password_list.append(random.choice(letters))

for char in range(0, in_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, in_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

newpass = ""

for newchar in password_list:
    newpass += newchar

print(f"Your new password is: {newpass}")