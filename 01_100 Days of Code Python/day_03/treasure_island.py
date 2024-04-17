from ascii_art import art

print(art)
print('Welcome to Treasure Island.\nYour mission is to find the treasure.\n')

user_choices = input('left or right? ').lower()

if user_choices == 'left':
    user_choices = input('swim or wait ').lower()

    if user_choices == 'wait':
        user_choices = input('which door? ').lower()

        if user_choices == 'red':
            print('Burned by fire.\nGame Over.')

        elif user_choices == 'blue':
            print('Eaten by beasts.\nGame Over.')

        elif user_choices == 'yellow':
            print('You Win!')

        else:
            print('Game Over.')

    else:
        print('Attacked by trout.\nGame Over.')

else:
    print('Fall into a hole.\nGame Over.')
