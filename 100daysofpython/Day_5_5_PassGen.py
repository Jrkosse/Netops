#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_bag = []

for letter in range(0,nr_letters):
    rd_index = random.randint(0,nr_letters)
    random_letter = letters[rd_index]
    password_bag.append(random_letter)

for number in range(0,nr_numbers):
    rd_index = random.randint(0,nr_numbers)
    random_number = numbers[rd_index]
    password_bag.append(random_number)

for symbol in range(0, nr_symbols):
    rd_index = random.randint(0,nr_symbols)
    random_symbol = symbols[rd_index]
    password_bag.append(random_symbol)

random.shuffle(password_bag)
final_password = ""
for item in password_bag:
    final_password += item
print(final_password)


