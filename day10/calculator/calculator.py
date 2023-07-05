from ascii_art import calc

print(calc)


def calculator(f_num, opr, s_num):
    if opr in mapper:
        return mapper[opr](f_num, s_num)


mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

first_number = float(input("What's the first number?: "))
for symbol in mapper.keys():
    print(symbol)

should_continue = True

while should_continue:

    operator = input("Pick an operation: ")
    second_number = float(input("What's next number?: "))
    result = calculator(first_number, operator, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")

    if input(f"Type 'Y'es to continue calculating with {result}, or type 'N'o to exit: ").lower() == "y":
        first_number = result
    else:
        should_continue = False
