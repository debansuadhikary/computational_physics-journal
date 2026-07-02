# taking the initials 
x = 0.2 # since we need to find log(1.2) by expanding log(1+x)
log_val = 0.0 # stores the summed up data 
term = x 
i = 1

while abs(term) > 0.00005:
    log_val += term
    i += 1
    term = ((-1)**(i-1))*(x**i)/i

print(f"log(1.2) = {log_val:.4f}")
