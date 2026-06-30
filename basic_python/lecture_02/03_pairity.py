# We are finding the number to be even or odd
# x = int(input("What's x? "))

# now formulating the logic of the code
# if x % 2 == 0:
#     print("Even")

# else:
#     print("Odd")

# We are going to implement the def function to make a function that tells us wether a number is odd or even
# defing the main function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# defining the number checking 'boolean' function
def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # since we have a boolean operator in our code itself so we do not need to worry about wether it would be true or not, infact we can just enter the condition to be checked 
    
    # return True if n % 2 == 0 else False
    
    return n % 2 == 0
    
# calling the main function 
main()