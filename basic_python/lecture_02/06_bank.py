# Taking greeting from the user
grt = input("Greeting: ").strip().lower()

# Checking for our program and returning the amount using the 'startswith' method of the string data type
if grt.startswith("hello"):
    print("$0")
elif grt.startswith("h"):
    print("$20")
else:
    print("$100") 
