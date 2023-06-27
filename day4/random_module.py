import random

num_one_range = int(input())
num_two_range = int(input())

random_integer = random.randint(num_one_range, num_two_range)
print(random_integer)


exclusive_num = int(input())  # exclusive value
random_float = random.random() * exclusive_num  # = 5 (0.00000... - 4.999999...)

print(random_float)
