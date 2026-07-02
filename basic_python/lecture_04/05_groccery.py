# building a dictionary for groccery list
groc_count = {}

# taking input from the user 
while True:
    try:
        item = input("Items: ").lower()
    except EOFError:
        break

    # checking for the frequency of every item
    if item in groc_count:
        groc_count[item] += 1
    else:
        groc_count[item] = 1

# sorting and printing the groccery list
for item in sorted(groc_count):
    print(groc_count[item], item.upper())