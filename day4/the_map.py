row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

split_coordinates = [int(x) for x in position]

row = split_coordinates[1] - 1
col = split_coordinates[0]

select_row = map[row]
select_row[col - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")



