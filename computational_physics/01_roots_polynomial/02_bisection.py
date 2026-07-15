# Bisection method for finding roots of a function
# defining a function whose root is to be found
def f(x):
    return x**3 - 2*x - 5

# defining the bisection function
def bisection(a, b, tol = 1e-4, max_iter = 100):
    fa = f(a)
    fb = f(b)

    if fa*fb >= 0:
        print("f(a) and f(b) must have opposite values.")
        return None
    
    for step in range(1, max_iter + 1):
        mid = (a + b)/2
        fmid = f(mid)

        if abs(fmid) < tol or (b - a)/2 < tol:
            print(f"Root found: {mid} in {step} steps.")
            return mid
        
        if fa*fmid < 0: # we are only interested in the part where sign change occurs
            b = mid
            fb = fmid
        else:
            a = mid
            fa = fmid

    print("Exceeded maximum iterations.")
    return None

# calling the bisection function
a0 = float(input("Enter the first number of the interval: "))
b0 = float(input("Enter the second number of the interval: "))

root = bisection(a0, b0)
