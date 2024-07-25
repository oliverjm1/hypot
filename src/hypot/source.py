# Requirements

# 2 inputs: positive, float
# 1 output: float
# external library? No external library


# Create a function - calculate hypot = sqrt(a^2 + b^2)
def hypot(a, b):
    """Function to return the hypotenuse of a triangle of side lengths provided

    Args:
        a (float): One triangle side length
        b (float): Other triangle side length

    Returns:
        float: hypotenuse of triangle
    """

    return sqrt(a**2 + b**2)


# Create a square root function : positive number - returns a float
def sqrt(a):
    """Return square root of a positive number

    Args:
        a (float): Positive number

    Returns:
        float: sqrt of a
    """

    return a**0.5


print(hypot(999, 3515))
