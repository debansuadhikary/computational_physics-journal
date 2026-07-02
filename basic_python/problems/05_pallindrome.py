# A pallindrome number is a number which reads the same from both sides.

# taking a number
n = (input("Enter a number: "))

# checking for pallindrome 
if n == n[::-1]:
    print("The number is a pallindrome number.")

else:
    print("The number is not a pallindromic number.")