# importing modules
import emoji

# taking input from the user
text = input("Input: ")

# printing the output
print("Output: ", emoji.emojize(text, language='alias'))
# "alias" means arbittary : for any emoji 