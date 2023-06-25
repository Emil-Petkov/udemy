age = input("What is your current age?")

age_in_int = int(age)

check_year = 100

days = (check_year * 365) - (age_in_int * 365)
weeks = (check_year * 52) - (age_in_int * 52)
months = (check_year * 12) - (age_in_int * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left to hundred years old.")
