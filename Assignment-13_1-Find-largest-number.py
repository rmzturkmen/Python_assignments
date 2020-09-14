# Find Largest Number in a List with function, for and if.

def max_num(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i
    else:
        return max


lst = [-6, 8, 12, 5, 13, -4]

print(max_num(lst))
