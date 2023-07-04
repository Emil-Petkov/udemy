from ascii_art import logo


print(logo)
print("Welcome to the secret auction program.")

participants_in_the_auction = {

}
while True:
    name = input("\nWhat is your name?: ").capitalize()
    bid = int(input("What's is your bid?: $"))

    participants_in_the_auction[name] = bid

    command = input("\nAre there any other bidders? Type 'Y'es or 'N'o: ").lower()
    if command == "y":
        continue
    elif command == "n":
        break

max_bid = 0

for name, bid in participants_in_the_auction.items():
    if participants_in_the_auction[name] > max_bid:
        max_bid = participants_in_the_auction[name]

        print(f"\nThe winner is {name} with a bid of ${max_bid}.")
