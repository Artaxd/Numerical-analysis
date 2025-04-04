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
        a = 0
        b = 3
        xn = (a+b)/2
        while np.abs(self.func(xn)) > error:
            if self.func(xn) * self.func(a) < 0:
                b = xn
            else:
                a = xn
            print(f"a = {a}, b = {b}, xn = {xn}, y = {self.func(xn)}")
            xn = (a+b)/2

        print(f"a = {a}, b = {b}, xn = {xn}, y = {self.func(xn)}")
        return xn
    
    def iterative_method(self, error=float("1e-3")):
        def g(x):
            return (6 - np.cos(x))/3
        
        xn = g(0)
        while np.abs(self.func(xn)) > error:
            print(f"xn = {xn}, f(xn) = {self.func(xn)}")
            xn = g(xn)

        print(f"xn = {xn}, f(xn) = {self.func(xn)}")

        return xn
    
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
        a = 0
        b = 3
        xn = a - (b-a)*(self.func(a))/(self.func(b) - self.func(a))
        while np.abs(self.func(xn)) > error:
            if self.func(xn) * self.func(a) < 0:
                b = xn
            else:
                a = xn
            print(f"a = {a}, b = {b}, xn = {xn}, y = {self.func(xn)}")
            xn = a - (b-a)*(self.func(a)/(self.func(b) - self.func(a)))

        print(f"a = {a}, b = {b}, xn = {xn}, y = {self.func(xn)}")
        return xn
    
    def secant_method(self, error=float("1e-3")):
        x0 = 0
        xn = 3
        while np.abs(self.func(xn)) > error:
            print(f"xn = {xn}, f(xn) = {self.func(xn)}")
            temp = xn
            xn = xn - self.func(xn)*((xn - x0)/(self.func(xn) - self.func(x0)))
            x0 = temp

        print(f"xn = {xn}, f(xn) = {self.func(xn)}")

        return xn
    
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


ea = eqAprox(f, f_prime, method="sec")

ea.solve()