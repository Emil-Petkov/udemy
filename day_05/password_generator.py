




from string import ascii_letters, digits, punctuation
import random

print('Welcome to the my password generator : )')


def password_generator(n_letters: int, n_symbols: int, n_numbers: int):
    generate_letters = [random.choice(ascii_letters) for _ in range(n_letters)]
    generate_symbols = [random.choice(punctuation) for _ in range(n_symbols)]
    generate_numbers = [random.choice(digits) for _ in range(n_numbers)]

    characters = generate_letters + generate_symbols + generate_numbers
    random.shuffle(characters)

    return f'Your password is: {''.join(characters)}'


try:
    n_letters = int(input('How many letters would you like in your password?\n'))
    n_symbols = int(input('How many symbols would you like?\n'))
    n_numbers = int(input('How many numbers would you like?\n'))
    print(password_generator(n_letters, n_symbols, n_numbers))

except ValueError as e:
    print(f'\nInput must be only numbers.\n{e}')
