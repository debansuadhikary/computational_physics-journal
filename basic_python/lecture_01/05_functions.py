# Here we will generate a new function by using 'def' function

def hello(to="world"):
    print("hello, ", to)

# If we call the function alone, we can see it accepts the default parameter as world 
# hello()

name = input("what is your name ?? ").strip().title()
hello(name)

# For the sake of writting huge programms we can define the main part of the program as a seperate function and call it upon usage

def main():
    name = input("What is your name ? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
