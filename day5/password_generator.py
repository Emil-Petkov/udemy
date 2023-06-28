import string
import random


def generate_password(how_many_latters: int, how_many_symbols: int, how_many_numbers: int):
    password = []

    def letters_in_password(how_many_latters: int):
        for _ in range(how_many_latter):
            password.append(random.choice(string.ascii_letters))

    def symbols_in_password(how_many_symbols: int):
        for _ in range(how_many_symbols):
            password.append(random.choice(string.punctuation))

    def numbers_in_password(how_many_numbers: int):
        for _ in range(how_many_numbers):
            password.append(random.choice(string.digits))

    letters_in_password(how_many_latters)
    symbols_in_password(how_many_symbols)
    numbers_in_password(how_many_numbers)

    random.shuffle(password)

    return ''.join(password)


print("Welcome to my Password Generator!\n")

how_many_latter = int(input("How many letters would you like in password: "))
how_many_symbols = int(input("How many symbols would you like: "))
how_many_numbers = int(input("How many numbers would you like: "))

print(f"\nHere is your password: {generate_password(how_many_latter, how_many_symbols, how_many_numbers)}")





