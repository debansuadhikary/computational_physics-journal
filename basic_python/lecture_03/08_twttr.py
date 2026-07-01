# taking input from the user 
long = input("Input: ")

short = ""

# checking and removing the vowels from the str
for char in long:
    if char.lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        short += char

print(f"Output: {short}")