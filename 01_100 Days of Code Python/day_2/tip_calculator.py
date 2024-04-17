print('Welcome to the tip calculator.')


def tip_calculator(bill: float, peoples: int, tip_percentage: int):
    if not tip_percentage == 0:
        per_person = bill / peoples + (bill / peoples * (tip_percentage / 100))
        return per_person

    return bill / peoples


bill = float(input('What was the total bill? $'))
peoples = int(input('How many people to spit the bill? '))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

sum_by_person = tip_calculator(bill, peoples, tip_percentage)

print(f'Each person should pay: ${sum_by_person:.1f}')
