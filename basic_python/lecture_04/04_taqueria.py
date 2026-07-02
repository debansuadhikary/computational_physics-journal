# dictionary of price of the food items
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
    try:
        # taking input from the user 
        food = input("Item: ").title()
    except EOFError:
        break # ctrl - z ends the loop
 
    if food in menu:
        price += menu[food]
        print(f"Total: ${price:.2f}")


    