import random

print("Welcome To Your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = int(input("Amount of passwords to generate: "))
length = int(input("Input your password length: "))

print("Here are your passwords:")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)  # Corrected variable name
    print(password)
