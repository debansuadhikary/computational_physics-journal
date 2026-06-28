# defining the main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# defining the first converstion function
def dollars_to_float(d):
    d = float(d.replace("$",""))
    return d

# defining the second conversion function
def percent_to_float(p):
    p = float(p.replace("%",""))
    return p/100

# calling the main function
main()