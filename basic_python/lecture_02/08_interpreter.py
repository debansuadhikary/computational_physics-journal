# taking the inputs from the user 
x, y, z = (input("Expression: ")).split()

# typecasting the variables 
x = int(x)
z = int(z)

# setting up the conditionals 
if y == "+":
    print(f"{x+z:.1f}")
elif y == "-":
    print(f"{x-z:.1f}")
elif y == "*":
    print(f"{x*z}")
elif y == "/" and z != 0:
    print(f"{x/z:.1f}")
else:
    print("no operator assigned")