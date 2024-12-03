import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

# for i in range(0, nr_letters):
#     index = random.randint(0, len(letters))
#     password += letters[i]
# for i in range(0, nr_symbols):
#     index = random.randint(0, len(symbols))
#     password += symbols[i]
# for i in range(0, nr_numbers):
#     index = random.randint(0, len(numbers))
#     password += numbers[i]
# print(password)

total_length = nr_letters + nr_symbols + nr_numbers
place = random.sample(range(0, total_length), nr_symbols + nr_numbers)
for i in range(0, total_length):
    if i in place:
        if nr_symbols > 0:
            password += random.choice(symbols)
            nr_symbols -= 1
        else:
            password += random.choice(numbers)
            nr_numbers -= 1
    else:
        password += random.choice(letters)
print(password)

# Shuffle the password will be more easy
password_list = []
for i in range(0, nr_letters):
    password.append(random.choice(letters))
for i in range(0, nr_symbols):
    password.append(random.choice(symbols))
for i in range(0, nr_numbers):
    password.append(random.choice(numbers))
shuffle(password_list)
print(password_list)