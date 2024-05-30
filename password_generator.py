import random
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '(', ')', '*']

print("Welcome to the Password Generator!")
n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

password_list = []

for _ in range(n_letters):
    password_list.append(random.choice(letters))

for _ in range(n_symbols):
    password_list.append(random.choice(symbols))

for _ in range(n_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your generated password is: {password}")
