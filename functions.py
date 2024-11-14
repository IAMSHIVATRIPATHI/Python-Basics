# Function to calculate the geometric mean
def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

# Function to check which number is greater
def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")

# Placeholder function to check which number is lesser
def isLesser(a, b):
    pass

# Test values
a = 9
b = 8

# Check which number is greater and calculate geometric mean
isGreater(a, b)
calculateGmean(a, b)

# Calculate geometric mean directly
gmean1 = (a * b) / (a + b)
print(gmean1)

# More test values
c = 8
d = 74

# Check which number is greater and calculate geometric mean
isGreater(c, d)
calculateGmean(c, d)

# Calculate geometric mean directly
gmean2 = (c * d) / (c + d)
print(gmean2)

# Function to calculate the average of three numbers with a default value for the third number
def average(a, b, c=1):
    print("The average is ", (a + b + c) / 2)

# Function to calculate the average of any number of arguments
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
    return sum / len(numbers)

# Calculate average with different sets of arguments
average(4, 6)
average(b=9)  # This will cause an error because the function expects positional arguments

# Calculate average with multiple arguments
c = average(5, 6, 7, 1)
print(c)

# Function to print a name using keyword arguments
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

# Print a name using keyword arguments
name(mname="Buchanan", lname="Barnes", fname="James")
