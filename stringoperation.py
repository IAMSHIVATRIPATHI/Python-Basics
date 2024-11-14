# Define a string with placeholders for formatting
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

# Using the format method to replace placeholders with variables
print(letter.format(country, name))

# Using f-strings for string interpolation
print(f"Hey my name is {name} and I am from {country}")

# Demonstrating how to include curly braces in f-strings
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

# Formatting a float to 2 decimal places using f-strings
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

# Demonstrating that f-strings result in a string type
print(type(f"{2 * 30}"))

# Define a function to calculate the square of a number
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

# Call the square function with 5
square(5)

# Print the docstring of the square function
print(square.__doc__)

# Example of a function with a detailed docstring
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

# Print the docstring of the add function
print(add.__doc__)

# Importing and printing The Zen of Python
import this
