# We are using the different boolean operators to assingn different operations to different conditions based on two different variables
x = int(input("What's x? "))
y = int(input("What's y? "))

# The if statements are used as conditional statements
if x < y:
    print("x is less than y")

# using another conditional statement making the entire workflow in mutually exclusive parts
elif x > y:
    print("x is greater than y")

# the else can only be used only once in a conditional program as it is the penultimate exclusive remaining condition
else:
    print("x is equal to y")

# we can infer the question about comparison in a different way :
# if x > y or y > x:
if x != y:
    print("x is not equal to y")

else:
    print("x is  equal to y")
