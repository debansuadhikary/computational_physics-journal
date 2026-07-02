# Anagrams are words consisting of the same consitituent letters. We will be using list to check for every letter.

# taking two strings
str_1 = str(input("Enter your first word: "))
str_2 = str(input("Enter your second word: "))

# taking a test parameter
test = 0

# using logic for checking anagrams 
for i in range (0, len(str_1)):
    if str_1[i] in str_2:
        test = 1

if test == 0:
    print("The two words are not Anagrams.")
else:
    print("The two words are Anagrams.")
