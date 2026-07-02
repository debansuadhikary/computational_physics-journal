# taking input from the user 
n = int(input("Enter a number: "))

# setting the first conditional
if n < 1:
    print(f"{n} is not a prime number.")

else:
    is_prime = True

    # setting the second conditional
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")