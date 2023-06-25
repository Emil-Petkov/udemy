def bmi_calculator(height: float, weight: float):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return f"\nYour BMI index is: {bmi:.2f} -> Underweight"
    elif bmi <= 24.9:
        return f"\nYour BMI index is: {bmi:.2f} -> Healthy"
    elif bmi < 30.0:
        return f"\nYour BMI index is: {bmi:.2f} -> Overweight"
    elif bmi <= 39.9:
        return f"\nYour BMI index is: {bmi:.2f} -> Obese"
    else:
        return f"\nYour BMI index is: {bmi:.2f} -> Severely Obese"



print("""
BMI Ranges:
 __________________________ 
| BMI < 18.5 Underweight   |
|__________________________|
| 18.5 - 24.9 Health       |
|__________________________|
| 25 - 29.9 Overweight     |
|__________________________|
| 30 - 39.9 Obese          |
|__________________________|
| BMI >= 40 Severely Obese |
| _________________________|
""")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

print(bmi_calculator(height, weight))
