# We are trying to make this programme more interesting and interactive by adding another function named 'input'

# "docs.python.org" is the source of all the info we need for learning more functions and their attributes

# The name is a variable that stores a return value and gives it when called upon 

name = input("What's your name ? ").strip().title()

# Removes white spaces from the str & capitalize the first letter of the str

# name = name.strip().capitalize()

# 'capitalize' just capitalises the first letter while 'title' capitalises the first letter of every word in a str, these attributes are known as "methods"

# name = name.strip().title()

print ("Hello, ", end="") 

# Here we are overwritting the default parameters set to the print with blank space

print (name)

# Or we can use a special string called format string to perform the above operation

print (f"hello, {name}")