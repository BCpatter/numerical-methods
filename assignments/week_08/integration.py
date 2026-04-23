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


def simpsons_rule(f, a, b, N):
    """
    Approximates the integral of a function f from a to b using Simpson's rule.

    Parameters:
    f: function
        The function to be integrated.
    a: float
        The lower limit of integration.
    b: float
        The upper limit of integration.
    N: int
        The number of slices (must be even).

    Returns:
    float
        The approximate value of the integral.
    """
    if N % 2 != 0:
        raise ValueError("N must be even for Simpson's rule.")

    h = (b - a) / N
    s = f(a) + f(b)
    k = 0.0

    # Sum for terms with weight 4 (odd indices)
    for i in range(1, N, 2):
        s += 4 * f(a + i * h)

    # Sum for terms with weight 2 (even indices)
    for i in range(2, N, 2):
        s += 2 * f(a + i * h)
    return (h / 3) * s

