# Armstrong number is a number that equals the sum of its own digits, each raised to the power of number of digits. 

# defining the armstrong checker
def armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    # implying the logic for checking the number is armstrong or not
    for d in digits:
        total += int(d)**power

    return total == n # this will check if the calculated total = original number and return a boolean

# testing for armstrong number
print(armstrong(153))
print(armstrong(370))
print(armstrong(123))