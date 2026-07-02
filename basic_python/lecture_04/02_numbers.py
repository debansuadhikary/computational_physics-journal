# we will use the following keywords to remove any future value error's possibility: 'try' & 'except'
# caller
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# calle
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            # x = int(input("What's x? "))
        except ValueError:
            pass
            # print("x is not integer")
        # else:
        #     return x

main()

# ValueError: invalid literal for int() with base 10: 'cat'
# the value error is prompted when we insert a different data type in place of the default programmed data type

# NameError: name 'x' is not defined
# it occurs when there is a variable in our code but we never defined it, as we can see here that due to type casting a wrong data type a value error occurs and we could not assign the 'str' to the x.