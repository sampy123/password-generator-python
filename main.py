import random

letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
           'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '@', '#', '$', '%', '&', '*', '?']

password_list = []

nb_letters = int(input("how many letters would you like in your password ?"))

nb_number = int(input("how many letters would you like in your password ?"))

nb_symbol = int(input("how many letters would you like in your password ?"))

for char in range(1, nb_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nb_number + 1):
    password_list.append(str(random.choice(numbers)))
for char in range(1, nb_symbol + 1):
    password_list.append(random.choice(symbols))

password = ""
random.shuffle(password_list)
for c in password_list:
    password += c
print(password)
