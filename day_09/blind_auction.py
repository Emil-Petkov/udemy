














from ascii_art import img

print(f'Welcome to the sicret auction.\n {img}\n')


def auction():
    peoples = {}

    while True:
        name = input('What is your name?: ').capitalize()
        bid = int(input("What's your bid?: "))

        peoples[name] = bid

        command = input("Are there any other bidders? Type 'yes' or 'no.'\n").lower()

        try:
            if command == 'no':

                max_value = max(peoples.values())
                winner = [name for name, value in peoples.items() if value == max_value]

                if len(winner) == 1:
                    print(f"\nThe winner is {winner[0]} with a bid of ${max_value}.")
                else:
                    winners_str = ", ".join(winner)
                    print(f"\nThere are multiple winners: {winners_str}, each with a bid of ${max_value}.")
                break

            elif command == 'yes':
                continue

            else:
                raise ValueError('Invalid command')

        except ValueError as e:
            print(e)
            break


auction()
