# defining the main function
def main():
    hrs = input("What time it is? ").strip()
    t = convert(hrs)

    # implementing the conditional statements 
    if 7.0<= t <= 8.0:
        print("Breakfast time")
    elif 12.0<= t <= 13.0:
        print("Lunch time")
    elif 18.0<= t <= 19.0:
        print("Dinner time")
    else:
        print("It's time to work")

# defining the convertor function 
def convert(hrs):
    if ":" in hrs:
        hours, minutes = hrs.split(":")
    else:
        hours, minutes = hrs, "0"
    
    # typecasting the variables
    hours = int(hours)
    minutes = int(minutes)

    # returning the value
    return hours + minutes / 60

main()
