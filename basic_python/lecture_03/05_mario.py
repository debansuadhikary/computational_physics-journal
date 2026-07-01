# an abstraction - a simplified overview of a complex problem and here we are trying to make a wall of three bricks by various methods we have learned 

# printing the vertical wall of bricks 

def main():
    print_column(3)

def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n"*height, end="")

main()

# printing the horizontal wall of bricks 

def main():
    print_row(4)

def print_row(width):
    print("?"*width)

main()

# printing a grid of bricks 

def main():
    print_square(3)

def print_square(size):

    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):
            print("#" * size)
        #     # print bricks
        #     print("#", end="")

        # print() # for changing the line of the briick

main()