# here we are trying to learn the various features of 'List', in which the contents are zero indexed i.e., they start with an index count of 0

students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)

# if we intend on using the numerical approach towards solving this problem, we may do this by the following way:
for i in range(len(students)):
    print(i+1, students[i])