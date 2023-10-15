def tip_calculator(bill, peoples, tip):
    calculate_tip_per_person = bill * (tip / 100)
    total_sum_per_person = (bill + calculate_tip_per_person) / peoples

    print(f"\nEach person should pay: ${total_sum_per_person:.1f}")


print("Welcome to the tip calculator.\n")

bill = float(input("What was the total bill? "))
peoples = int(input("How many people to split bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))

tip_calculator(bill, peoples, tip)
