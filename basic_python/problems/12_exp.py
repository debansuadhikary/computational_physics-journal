# setting the initials
x = 1.5 # the value of x in {e^x}
exp_val = 1.0 # first element of the series of e^x
term = 1.0 # number of terms
i = 1 # factorial denominator 

while term >= 0.0005:
    term *= x/i
    exp_val += term
    i += 1

print(f"exp(1.5) = {exp_val:.3f}")