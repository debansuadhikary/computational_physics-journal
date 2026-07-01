# here we are learning dictionaries : they are a documented relation between keys and values, a more 2-dimensional approach to store data

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin"
#     }

# # as default the 'for' loop gives us the keys of the dictionary
# for student in students:
#     print(student, students[student], sep=": ")

# Now we are going to understand list of dictionries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")