print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_bill = 0

price_for_size = {
    "S": 15,
    "M": 20,
    "L": 25,
}

peperoni = {
    "S": 2,
    "M": 3,
    "L": 3,
}

cheese = {
    "Y": 1,
}

if size in price_for_size:
    total_bill += price_for_size[size]

    if add_pepperoni == "Y":
        total_bill += peperoni[size]

    if extra_cheese == "Y":
        total_bill += cheese["Y"]

print(f"Your final bill is: {total_bill}")


################################################################

print("Welcome to Python Pizza Deliveries!")

SIZE_PRICES = {"S": 15, "M": 20, "L": 25}
PEPPERONI_PRICES = {"S": 2, "M": 3, "L": 3}
EXTRA_CHEESE_PRICE = 1

while True:
    size = input("What size pizza do you want? S, M, or L: ")
    if size in SIZE_PRICES:
        break
    else:
        print("Invalid input. Please enter S, M, or L.")

while True:
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    if add_pepperoni in ["Y", "N"]:
        break
    else:
        print("Invalid input. Please enter Y or N.")

while True:
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese in ["Y", "N"]:
        break
    else:
        print("Invalid input. Please enter Y or N.")

total_bill = 0

try:
    total_bill += SIZE_PRICES[size]

    if add_pepperoni == "Y":
        total_bill += PEPPERONI_PRICES[size]

    if extra_cheese == "Y":
        total_bill += EXTRA_CHEESE_PRICE
except KeyError:
    print("An error occurred. Please try again.")

print(f"Your final bill is: {total_bill}")


