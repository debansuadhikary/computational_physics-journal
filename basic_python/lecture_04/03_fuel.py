while True:
    try:
        # taking input as fraction
        x, y = map(int, input("Fraction: ").split("/")) 
        # this splits both the variables at the same time
        if x > y or y == 0:
            continue
        # giving output as percentage
        z = (x / y) * 100
        break

    except (ValueError, ZeroDivisionError):
        continue
    

# initialising the conditionals
if z <= 1 :
    print("E")
elif z < 99 :
    print(round(z), "%", sep="")
else:
    print("F")

