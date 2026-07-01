# understanding repetative actions with loops : while loop which allows us to ask with a boolean expression
i = 3
while i != 0:
    # while the condition fullfills: do this function
    print("meow")
    i = i-1

# In case we find ourselves in an infinite loop, just use Ctrl + C in order to interupt the operation 

# Even we can do this in the other way around by incrementing our assigning variable
i = 0
while i < 3:
    print ("bark")
    i += 1

# for loop : we are using this in accordance with lists which are literally list of items stored in []

#for i in [0,1,2]:
for _ in range(3):
    print("hoof")

# for loop is best suited when we know the number of iterations that are going to be performed 
# the number given in range will be specified as the limit of the repitation frequency as the loop does not exceeds the given limit

# we can even loop the task by multiplying it to the number of itterations that we want

print("quack\n"*3, end="")
