import numpy as np

def f(x):
    return np.cos(x) + 3*x - 6

def f_prime(x):
    return -np.sin(x) + 3

class eqAprox:
    """
    Approximates an equation with given method:
    "bise" - Bisection
    "iter" - Iterative
    "newt" - Newton's method
    "chor" - Method of chords
    "sec" - Secant method

    default - Newton's method
    """
    def __init__(self, func, func_prime, method="newt"):
        """
        func - The function whose root we are trying to find
        func_prime - derivative of given the function
        method - method of approximation
        """
        self.func = func
        self.func_prime = func_prime
        self.method = method

    def bisection_method(self, error=float("1e-2")):
        return
    
    def iterative_method(self, error=float("1e-3")):
        return
    
    def newtons_method(self, error=float("1e-3")):
        #initial guess
        xn = 0
        #calculate function's value and it derivative's value at xn
        y = self.func(xn)
        y_prime = self.func_prime(xn)

        while np.abs(y) > error:
            print(f"xn = {xn}, f(xn) = {y}")
            #find next guess
            xn = xn - y/y_prime

            #find new values of y and y_prime
            y = self.func(xn)
            y_prime = self.func_prime(xn)

        print(f"xn = {xn}, f(xn) = {y}")

        return xn

    def method_of_chords(self, error=float("1e-3")):
        return
    
    def secant_method(self, error=float("1e-3")):
        return
    
    def solve(self):
        match self.method:
            case "bise":
                self.bisection_method()
            case "iter":
                self.iterative_method()
            case "newt":
                self.newtons_method()
            case "chor":
                self.method_of_chords()
            case "sec":
                self.secant_method()
            case _:
                print("wrong method")


ea = eqAprox(f, f_prime)

ea.solve()