import random
import string
letters = list(string.ascii_letters)
digits = list(string.digits)
symboles = list(string.punctuation)
# print(letters)
# print(digits)
# print(symboles)

print("Welcome to the password generator!!")
pass_gen_letter = int(input("how many letters would you like in your password! "))
pass_gen_digits = int(input("how many digits would you like in your password! "))
pass_gen_symbols = int(input("how many symbols would you like in your password! "))

password_list = []

for i in range(0, pass_gen_letter):
    password_list += random.choice(letters)

for i in range(0, pass_gen_digits):
    password_list += random.choice(digits)

for i in range(0, pass_gen_symbols):
    password_list += random.choice(symboles)

random.shuffle(password_list)
#print(password_list)

password = ''
for j in password_list:
    password += j

print(password)
