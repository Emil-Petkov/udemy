from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """Check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1

    elif guess < answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {answer}")


def set_difficultly():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    try:
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS

        raise ValueError("Invalid input")
    except ValueError as e:
        print(e)
        exit()


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    answer = randint(1, 100)

    turns = set_difficultly()

    guess = 0
    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("\nYou've run out of guesses, you lose.\n")
            print(f"The number was: {answer}")
            return


game()

########################################################################################################################


# import random
#
# random_number = random.randint(1, 100)
#
#
# def difficultly_level(level: str):
#     counter = 0
#     try:
#
#         if level in ["easy", "hard"]:
#
#             if level == "easy":
#                 print("\nYou have 10 attempts remaining to guess the number.\n")
#                 counter = 10
#
#             elif level == "hard":
#                 print("\nYou have 5 attempts remaining to guess the number.\n")
#                 counter = 5
#
#             while counter > 0:
#
#                 number = int(input("Make a guess: "))
#                 if random_number == number:
#                     print(f"You WIN! The number was: '{random_number}' :)")
#                     exit()
#
#                 elif random_number > number:
#                     print("Too low.")
#
#                 elif random_number < number:
#                     print(f"Too high.")
#
#                 counter -= 1
#                 if counter == 0:
#                     break
#                 else:
#                     print(f"""\nYou have {counter} attempts remaining to guess the number.\n""")
#
#             print(f"\nYou lose the number was: {random_number}")
#
#         raise ValueError("Invalid choice!")
#
#     except ValueError as e:
#         print(e)
#
#
# print("""Welcome to Number Guessing Game!\n
# I'm thinking of a number between 1 and 100.""")
#
# choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# difficultly_level(choose)






