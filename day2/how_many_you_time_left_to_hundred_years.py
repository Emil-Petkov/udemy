age = int(input("What is your current age?"))

check_year = 100

days = (check_year * 365) - (age * 365)
weeks = (check_year * 52) - (age * 52)
months = (check_year * 12) - (age * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left to hundred years old.")
