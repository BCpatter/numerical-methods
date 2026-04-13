# Students should edit this Python file (just as you would a Python cell in a Jupyter Notebook)
# this module will contain functions for numerical integration


def trapezoidal_rule(f, a, b, N):

    """
    Approximates the integral of a function f from a to b using the trapezoidal rule.
    
    parameters: 
    f: function
    The function to be integrated.
    def trapezoidal_rule(f, a, b, N):
    a: float
    The lower limit of integration.
    b: float
    The upper limit of integration.
    N: int
    The number of slices

    Returns:
    float
    The approximate value of the integral
    """
    
    h = (b - a) / N
    total = 0.5 * f(a) + 0.5 * f(b)

    s = 0

    for k in range(1, N):
        s += f(a + k * h)
 
    return h * s


def simpsons_rule():
    #write the arguments, docstring, and actual code of this function

    return