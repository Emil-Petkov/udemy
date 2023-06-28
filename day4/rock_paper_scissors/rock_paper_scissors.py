import random

from ascii_art import rock, paper, scissors

mapping = {
    "r": rock,
    "p": paper,
    "s": scissors
}
player_choose = input("Choice 'r'ock, 'p'aper or 's'cissors : ").lower()

while True:

    try:
        if player_choose in mapping:
            print(f"\nPlayer Choice: {mapping[player_choose]}")
            break

        else:
            raise KeyError("Invalid choice.")

    except KeyError as e:
        print(f"\n{e} Try again.\n")

    player_choose = input("Choice 'r'ock, 'p'aper or 's'cissors : ").lower()

pc_choose = random.choice(["r", "p", "s"])

print(f"Computer chose: {mapping[pc_choose]}")

if player_choose == "r" and pc_choose == "r":
    print("Draw")
elif player_choose == "p" and pc_choose == "p":
    print("Draw")
elif player_choose == "s" and pc_choose == "s":
    print("Draw")
elif player_choose == "r" and pc_choose == "s":
    print("You Win")
elif player_choose == "r" and pc_choose == "p":
    print("You Lose")
elif player_choose == "p" and pc_choose == "r":
    print("You Win")
elif player_choose == "p" and pc_choose == "s":
    print("You Lose")
elif player_choose == "s" and pc_choose == "p":
    print("You Win")
elif player_choose == "s" and pc_choose == "r":
    print("You Lose")

