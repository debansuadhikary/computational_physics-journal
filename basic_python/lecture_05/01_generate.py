# there are various libraries in python, that contains code for pre-solved problems that are used repeatedly
# each library contains a set of modules, where each module contains some pre-defined tools that we as users may use in our code

# import random
from random import choice

# coin = random.choice(["heads","tails"])
# print(coin)
coin = choice(["heads", "tails"])
print(coin)

# for getting a random number within a range we use randint(a,b) function as follows
import random

number = random.randint(1,10)
print(number)

# also we have another function as shuffle(x), to randomise the items in a list
import random 

cards = ["A1", "B1", "C1"]
random.shuffle(cards)
for card in cards:
    print(card)
