# Fibonacci series is a series having the subsequent digits as the sum of the previous two. Here we will print a list of 10 terms

# initialising the number of terms to be printed 
n = 10

# taking the starting and ending number 
a = int(input("Enter the starting number: "))
b = int(input("Enter the second number: "))

print(a, b, end = " ")

for _ in range(n - 2):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c
