# taking input from the user 
camel = input("camelCase: ")
snake = ""

# converting the variable 
# '.isupper' checks wether the letter is uppercased or not
for char in camel:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char
        
# giving up the output
print(f"snake_case: {snake}")