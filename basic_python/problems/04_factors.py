# taking the input 
n = int(input("Enter a number: "))

# creating an empty list
l = []

print(f"Factors of {n} are: ")
for i in range(1, n+1):
    if n % i == 0:
        l.append(i)

print(l)