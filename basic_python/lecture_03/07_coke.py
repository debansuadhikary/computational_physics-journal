# getting the initial value of coke
amount_due = 50

# initialising an infinite loop
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    # checking if the coin is valid 
    if coin in [25, 10, 5]:
        amount_due -= coin

# loop ending 
print(f"Change Owed: {abs(amount_due)}")