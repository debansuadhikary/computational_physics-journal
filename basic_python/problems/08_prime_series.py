# taking the input 
n1 = int(input("Enter lower range: "))
n2 = int(input("Enter higher range: "))

# creating two empty lists
pr = []
npr = []

# finding primes
for i in range(n1, n2+1):
    if i <= 1:
        npr.append(i)
    else:
        is_prime = True

        for j in range(2, int(i**0.5)+1): # if j*j > i then the logic would be meaningless 
            if i % j == 0:
                is_prime = False
                break
            
        if is_prime:
            pr.append(i)
        else:
            npr.append(i)

print(f"The prime number between {n1} and {n2} are: \n{pr}")
print(f"The non-prime number between {n1} and {n2} are: \n{npr}")