# Find Largest and Smallest Number.

num = 0
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'exit':
        break
    try:
        numx = int(num)
    except:
        print("invalid input")
        continue
    if largest is None or numx > largest:
        largest = numx
    if smallest is None or numx < smallest:
        smallest = numx

print("Maximum is", largest)
print("Minimum is", smallest)
