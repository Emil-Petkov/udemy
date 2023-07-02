import random
from words import list_of_words
from ascii_hangman import stages, logo

pc_random_word = random.choice(list_of_words)
hidden_word = ["_" for _ in range(len(pc_random_word))]

display = []

lives = 6

end_of_game = False

print(logo)

while not end_of_game:
    print(' '.join(hidden_word))

    guess = input("\nGuess a letter: ").lower()

    if guess in hidden_word:
        print(f"You've already guessed '{guess}'")

    for position in range(len(pc_random_word)):
        letter = pc_random_word[position]
        if letter == guess:
            hidden_word[position] = letter

    if guess not in pc_random_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True

    print(' '.join(hidden_word))

    if "_" not in hidden_word:
        end_of_game = True

    print(stages[lives])

if lives > 0:
    print("You win.")
else:
    print(f"""Тhe word was '{pc_random_word}.'\nYou lose. Good luck next time.""")
