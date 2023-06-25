def sum_per_person(bill: float, peoples: int, percent: float):
    calculate = bill + bill * (percent / 100)
    return f"Each person should pay: ${calculate / peoples:.2f}"


print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $ "))
peoples = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? "))

print(sum_per_person(total_bill, peoples, percent))
