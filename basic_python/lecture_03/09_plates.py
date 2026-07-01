# # defining the main function
# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# # defining the critical function
# def is_valid(s):
#     # Rule_1: .isalpha() checks wether the charachter is alphabet or not
#     if not (s[0].isalpha() and s[1].isalpha()):
#         return False
    
#     # Rule_2:
#     if not (2 <= len(s) <= 6):
#         return False
    
#     # Rule_4: we will use .isalnum() as it checks that every char in the string is either number or alphabet
#     if not s.isalnum():
#         return False
    
#     # Rule_3:
        

# define the main function to check whether is_valid is satisfied
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# defining the secondary function based on False approach : if the function itself returns False then the secondary function also returns False
def is_valid(s):
    if not length(s):
        return False
    if not two_letters(s):
        return False
    if not alphanumeric(s):
        return False
    if not numberatend(s):
        return False
    if not no_zero_begins(s):
        return False
    return True

# definig the tertiary functions

def two_letters(s):
    if len(s)<2:
        return False
    # if len(s)>2: it further checks that wether the first and second letters are alphabets or not
    return s[0].isalpha() and s[1].isalpha()

def length(s):
    return (2<=len(s)<=6)

def alphanumeric(s):
    return s.isalnum()

def numberatend(s):
    # taking a preliminary assumption
    n= False
    for char in s:
        if char.isdigit():
            n=True
        elif n and char.isalpha():
            return False
    return True

# enumerate returns us the pair of charachters and the index of the charachters
def no_zero_begins(s):
    for i, char in enumerate(s):
        if char.isdigit():
            return char != "0"   # First digit should not be '0'
    return True  # No numbers at all is fine


main()