# We are trying to make an interactive calculator by taking an input from the user and storing it in two variables 

# Input function stores the value as str and thus we need to convert the data type from 'str' to 'int' by "nesting functions" - the inside gets worked out first before the outside

x = float(input("What's x ?? "))

y = float(input("What's y ?? "))

# Here we are rounding things up in two different approaches:
z = round(x+y, 2)
# print(z)

# z = x + y
# print(f"{z:.2f}")

# Here we are adding commas in our number to differentiate between different place values of a number: 
# z= x+y
print(f"{z:,}")

# Or we can nest the entire code in a single line 

# print(float(input("What's x ?? ")) + float(input("What's y ?? "))) 

# If we try to define a function so that it squares a given number we can do it by :

def main():
    x = int(input("What's x? "))
    print("x sqaured is", square(x))

def square(n):
    return n*n

main()
