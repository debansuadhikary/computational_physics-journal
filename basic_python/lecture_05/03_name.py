# here we will learn about command line arguments - vis 'sys' library which are values you can pass to a Python script when you run it from the terminal or command prompt. 
# where sys.argv is accronymn for argumented vector which stores the input in the form of a list. The "sys.argv[0]" stores the name of the program

import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# main code
print("hello, my name is", sys.argv[1])

# if we do not insert our name in this case, we may encounter 'IndexError: list index out of range'

# Again if we try to write many names in our command line, we may do it by the following way :

# for arg in sys.argv:
#     print("hello, my name is", arg)

# This will also give us the name of the file indexed at 0th position, in order to encounter this we need to 'slice' the list i.e., a subset of the list 

for arg in sys.argv[1:]:
     print("hello, my name is", arg)