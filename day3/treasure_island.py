print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


def first_choice_func(first_choice):
    while True:
        try:
            if first_choice in mapping:
                if first_choice == "right":
                    print(f"\n{mapping[first_choice]}")
                    exit()
                else:
                    break
            else:
                raise KeyError("Invalid command")

        except KeyError as e:
            print(f"{e} Try again.\n")
            first_choice = input("Choice left or right: ").lower()


def second_choice_func(second_choice):
    while True:
        try:
            if second_choice in mapping:
                if second_choice == "swim":
                    print(f"\n{mapping[second_choice]}")
                    exit()
                else:
                    break
            else:
                raise KeyError("Invalid command")

        except KeyError as e:
            print(f"{e} Try again.\n")
            second_choice = input("Swim or wait boat: ").lower()


def third_choice_func(third_choice):
    while True:
        try:
            if third_choice in mapping:
                if third_choice in ["red", "blue", "yellow"]:
                    print(f"\n{mapping[third_choice]}")
                    exit()
            else:
                raise KeyError("Invalid command")

        except KeyError as e:
            print(f"{e} Try again.\n")
            third_choice = input("Which door -> (Red, Blue or Yellow): ").lower()


mapping = {
    "left": second_choice_func,
    "right": "Fall into a hotel.\nGame Over.",
    "wait boat": third_choice_func,
    "swim": "Attacked by trout.\nGame Over.",
    "red": "Burned by fire.\nGame Over.",
    "blue": "Eaten by beasts.\nGame Over.",
    "yellow": "You Win!",
}

print("""Welcome to Treasure Island.
Your mission is to find the treasure.
_____________________________________\n""")

first_choice = input("Choice left or right: ").lower()
first_choice_func(first_choice)

second_choice = input("Swim or wait boat: ").lower()
second_choice_func(second_choice)

third_choice = input("Which door -> (Red, Blue or Yellow): ").lower()
third_choice_func(third_choice)
