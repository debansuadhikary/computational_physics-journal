# The program tries to cover the other conditional operators with another task of assigning grades of different students

# taking input from the user 
score = int(input("Score: "))

# our conditional workflow
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# We can tidy things up a bit more in the following way
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60<= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Or if we assume some preliminaries before hand then we can do the following thing
if score >= 90 :
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")