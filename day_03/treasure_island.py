from ascii_art import treasure

print(treasure + "\nWelcome to Treasure Island.\n"
      "Your mission is to find the treasure.")

first_choice = input("You're at a cross road." + 'Where do you want to go? Type "left" or "right"\n')
if first_choice == "right" or first_choice == "Right" or first_choice == "RIGHT":
    print("Fall into a hole.\nGame Over.")

elif first_choice == "left" or first_choice == "Left" or first_choice == "LEFT":
    second_choice = input('You come to a lake. There is an island in the middle fo the lake. Type "wait" to wait'
                          'for a boat. Type "swim" to swim across.\n')

    if second_choice == "swim" or second_choice == "Swim" or second_choice == "SWIM":
        print("Attacked by trout.\nGame Over.")
    elif second_choice == "wait" or second_choice == "Wait" or second_choice == "WAIT":
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow "
                             "and one blue. Which colour do you choose?\n")
        if third_choice == "yellow" or third_choice == "Yellow" or third_choice == "YELLOW":
            print("You Win!")
        elif third_choice == "red" or third_choice == "Red" or third_choice == "RED":
            print("Burned by fire.\nGame Over.")
        elif third_choice == "blue" or third_choice == "Blue" or third_choice == "BLUE":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")

    else:
        print("Attacked by trout.\nGame Over.")

else:
    print("Fall into a hole.\nGame Over.")
