# Find Largest Number in a List with for loop.

lst = [-6, 8, 12, 5, 13, -4]

max_num = lst[0]

for i in range(1, len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]

print(max_num)
