n = 10

for i in range(0, n): # Here we are taking row number
    for j in range(0, i+1): # Here we are taking column number, and it is increasing per row 
        print("*", end=" ")
    print() # this line is used to shift into the next line
print()

for i in range(0, n):
    for j in range(0, n-i): # Here we are reducing the columns one by one
        print("*", end=" ")
    print()
print()

for i in range(0, n):
    for j in range(0, i): # it will create the blank places just left side of the "*"
        print(end=" ") # here we are just nudging the cursor to the right and not moving towards the next line 
    for j in range(i+1, n): # it will create the pattern
        print("*", end=" ")
    print()
print()

for i in range(0, n): # this is just the inverse of the previous pattern 
    for j in range(0, n-i):
        print(end=" ")
    for j in range(n-i+1, n):
        print("*", end=" ")
    print()
print()
