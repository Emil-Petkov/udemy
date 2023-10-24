import random
from ascii_art import rock, scissors, paper

player_choice = input("Choice 'r'ock, 's'cissors or 'p'aper: ").lower()

mapping = {
    'r': rock,
    's': scissors,
    'p': paper
}

pc_choice = random.choice(list(mapping.keys()))

print("Player's choice:")
print(mapping[player_choice])
print("\nPC's choice:")
print(mapping[pc_choice])

if player_choice == pc_choice:
    print("Draw")
elif (player_choice == 'r' and pc_choice == 's') or \
        (player_choice == 's' and pc_choice == 'p') or \
        (player_choice == 'p' and pc_choice == 'r'):
    print('Player Win')
else:
    print('Player Lose')
