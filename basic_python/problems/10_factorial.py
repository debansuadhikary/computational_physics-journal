from math import prod
# taking input
n = int(input("Enter a number: "))

# OLD LOGIC
# # setting a dummy variable
# fact = 1

# # applying the logic
# for _ in range(1, n+1):
#     fact *= _

# NEW LOGIC
fact = prod(range(1, n+1))

# printing out the results
print(f"Factorial of {n} is {fact}.")