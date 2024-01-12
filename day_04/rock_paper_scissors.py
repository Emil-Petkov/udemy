import random
from ascii_art import rock, paper, scissors


def rock_paper_scissors(choice: str):
    if choice not in ('r', 'p', 's'):
        raise ValueError("Invalid input. Please choose: 'r', 'p', or 's'.")

    player = choice
    computer = random.choice(['r', 'p', 's'])

    if player == 'r' and computer == 'r':
        print(f'\nYou: {rock}')
        print(f'Computer chose: {rock}\n')

        return 'Draw'

    elif player == 'r' and computer == 's':
        print(f'\nYou: {rock}')
        print(f'Computer chose: {scissors}\n')

        return 'You Win'

    elif player == 'r' and computer == 'p':
        print(f'\nYou: {rock}')
        print(f'Computer chose: {paper}\n')

        return 'You Lose'

    elif player == 'p' and computer == 'p':
        print(f'\nYou: {paper}')
        print(f'Computer chose: {paper}\n')

        return 'Draw'

    elif player == 'p' and computer == 'r':
        print(f'\nYou: {paper}')
        print(f'Computer chose: {rock}\n')

        return 'You Win'

    elif player == 'p' and computer == 's':
        print(f'\nYou: {paper}')
        print(f'Computer chose: {scissors}\n')

        return 'You Lose'

    elif player == 's' and computer == 's':
        print(f'\nYou: {scissors}')
        print(f'Computer chose: {scissors}\n')

        return 'Draw'

    elif player == 's' and computer == 'p':
        print(f'\nYou: {scissors}')
        print(f'Computer chose: {paper}\n')

        return 'You Win'

    elif player == 's' and computer == 'r':
        print(f'\nYou: {scissors}')
        print(f'Computer chose: {rock}\n')

        return 'You Lose'


try:
    player_choice = input("What do you choose?\n"
                          "Type 'r'ock, 'p'aper or 's'cissors: ").lower()

    print(rock_paper_scissors(player_choice))
except ValueError as e:
    print(e)
