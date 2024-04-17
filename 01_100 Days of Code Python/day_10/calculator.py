def calculator(f_num: float, operator: str, s_num: float):
    if s_num == 0 and operator in ['/', '//', '%']:
        return 'Divide by Zero.'

    mapper_operation = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
    }

    if operator in mapper_operation:
        return mapper_operation[operator](f_num, s_num)

    else:
        raise ValueError('Invalid operator.')


first_number = float(input('First number: '))
operation = input('Operation ')
second_number = float(input('Second number: '))

try:
    result = calculator(first_number, operation, second_number)
    print(f'Result is: {result}')

except ValueError as e:
    print(e)
