# Now we are trying to learn about spliting a string and storing it in a different variables in order to call them separately when required

name = input("What is your name?").strip().title()

# Here we are spliting the user's name into two separate variables and the split is performed over the space charachter 

first, last = name.split(" ")

print (f"hello, {first}")
