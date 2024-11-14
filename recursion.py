# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# The factorial of a number n is the product of all positive integers less than or equal to n.
# It is denoted by n! and is defined as:
# factorial(n) = n * factorial(n-1)

def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if (n == 0 or n == 1):
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Test the factorial function with an example
print(factorial(5))  # Output should be 120


# Quick Quiz: Write a program to print the Fibonacci sequence
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# It starts with 0 and 1.
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# Example Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the fibonacci function with an example
for i in range(10):
    print(fibonacci(i), end=" ")  # Output should be 0 1 1 2 3 5 8 13 21 34