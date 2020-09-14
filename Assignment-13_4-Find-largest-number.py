# Find Largest Number in a List with sort.
# Write a code that specifies how many numbers to enter the list.

lst = []
num = int(input("Please enter the total number of the list: "))

for i in range(1, num + 1):
    val = int(input(f"Please enter {i} number: "))
    lst.append(val)

lst.sort()
# lst.reverse()

print("The largest number in the list is: ", lst[-1])
# print("The largest number in the list is: ", lst[0])
