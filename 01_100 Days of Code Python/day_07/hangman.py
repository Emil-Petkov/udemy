import random
from ascii_art import art
from list_of_words import words

current_word = random.choice(words)
display = ['_' for _ in range(len(current_word))]
print(art[0])
print(' '.join(display))


def hangman():
    counter = 0
    end_of_game = False

    while not end_of_game and counter < 6:
        guess = input('\nGuess a letter: ').lower()

        if not guess.isalpha() or len(guess) > 1:
            print('Input must be a single letter.')
            continue

        if guess in current_word:
            for position in range(len(current_word)):
                if current_word[position] == guess:
                    display[position] = guess

        else:
            counter += 1
            print(art[counter])

        print(' '.join(display))

        if '_' not in display:
            end_of_game = True
            print('\nYou Win!')

    if counter == 6:
        print('You Lose : (\n')
        print(f'The word was: {current_word}')


try:
    hangman()

except ValueError as e:
    print(e)
