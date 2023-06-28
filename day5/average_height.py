from typing import List


def calculate(storage_info, len_data):
    return sum(storage_info) / len_data


def average_height(data: List[str]):
    storage_info = [int(x) for x in data]
    len_data = len(storage_info)
    return calculate(storage_info, len_data)


data = input().split()

print(average_height(data))
