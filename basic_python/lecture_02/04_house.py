# here we are trying to plot a relationship between two sets: one is the house and the other is who lives there w.r.t Harry Potter Lore

name = input("what's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who??")

# we can do this in a more systamatic way by using another operator 'match':
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")