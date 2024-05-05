import random


def game():
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = 10 if level == 'easy' else 10

    answer = random.randint(1, 100)

    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')

        try:
            guess = int(input('Make a guess: '))

        except ValueError:
            print('Please enter a valid number.')
            continue

        if guess == answer:
            print(f'Congratulations! You Win.')
            return

        elif guess > answer:
            print('Too high.')

        else:
            print('Too low.')

        attempts -= 1

    print(f'You have {attempts} attempts remaining to guess the number.')


game()
