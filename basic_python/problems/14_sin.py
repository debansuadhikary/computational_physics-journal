import math
x = math.radians(25)

# taking the initials
sin_val = x
term = x
i = 1

while abs(term) > 0.001:
    term *= (-1)*x**2 / ((2*i)*(2*i+1))
    sin_val += term
    i += 1

print(f"sin(25) = {sin_val:.3f}")