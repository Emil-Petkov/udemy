import random, string

print("Welcome to the my Password Generator.")


def password_generator(l, s, n):

    letter_list = [random.choice(string.ascii_letters) for _ in range(l)]
    symbol_list = [random.choice(string.punctuation) for _ in range(s)]
    numbers_list = [random.choice(string.digits) for _ in range(n)]

    password = letter_list + symbol_list + numbers_list
    random.shuffle(password)
    return ''.join(password)


letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

print(f"Here is your password: {password_generator(letters, symbols, numbers)}")
