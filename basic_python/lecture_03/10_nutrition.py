# we will be tackling this problem with the help of dictionaries
fruits = {
    "Apples": 130, "Avocado": 50, "Banana": 110,
    "Cantaloupe": 50, "Garpefruit": 60, "Grapes": 90,
    "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15,
    "Lime": 20, "Nectarine": 60, "Orange": 80,
    "Peach": 60, "Pear": 100, "Pineapple": 50,
    "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100,
    "Tangerine": 50, "Watermelon": 80
}

# taking input from the user 
item = input("Item: ").title()
calories = fruits.get(item)
if calories:
    print(f"Calories: {calories}")

# setting up the condition
# if item in fruits:
#     print(f"Calories: {fruits[item]}")