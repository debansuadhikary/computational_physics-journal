# taking input from the user 
str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

# setting up the conditionals 
if str == "42" or str == "forty-two" or str == "forty two":
    print("Yes")
else:
    print("No")