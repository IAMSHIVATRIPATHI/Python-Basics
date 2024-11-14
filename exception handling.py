# Exception Handling
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")

# Finally Clause
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed")

x = func1()
print(x)

# Raising Custom Errors
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

class CustomError(Exception):
    pass

try:
    a = int(input("Enter any value between 5 and 9: "))
    if a < 5 or a > 9:
        raise CustomError("Value should be between 5 and 9")
except CustomError as e:
    print(e)

# If ... Else in One Line
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a > b else 0
print(c)
