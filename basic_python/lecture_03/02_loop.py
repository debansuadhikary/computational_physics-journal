# using the loop function but we need to take the number of iterations allowed from the user, taking into considerations that the user might give the most generalised number from (-infinity:infinity)

# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# lets define this entire process as a function
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main()