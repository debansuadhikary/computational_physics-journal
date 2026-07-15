# Newton-Rhapson Method for Finding Roots of a Function
# defining a function and its derivative
def f(x):
    # function whose root we want to find
    return x**3 - x**2 -1

def Df(x):
    # Derivative of the function
    return 3*x**2 - 2*x

# defining the Newton-Rhapson method for finding a root of f(x) = 0
# x0: initial guess
# tol : tolerance for stopping criterion
# max_iter : maximum number of iterations
def newton(x0, tol = 1e-10, max_iter = 100):
    xn = x0

    for step in range(1, max_iter + 1):
        fxn = f(xn)

        if abs(fxn) < tol:
            print(f"Root found: {xn} in {step} steps.")
            return xn
        
        Dfxn = Df(xn)

        if Dfxn == 0:
            print("Derivative is zero. Newton's method fails.")
            return None
        
        xn = xn - fxn/Dfxn
    
    print("Exceeded maximum iterations. No solutions found.")
    return None

# calling the Newton-Rhapson method
x0 = float(input("Enter initial guess: "))
max_iter = int(input("Enter maximum number of iterations: "))

root = newton(x0, tol = 1e-10, max_iter = max_iter)
