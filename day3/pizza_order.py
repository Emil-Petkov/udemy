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
