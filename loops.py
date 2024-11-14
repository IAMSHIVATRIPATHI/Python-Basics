name = 'Abhishek'
for i in name:
    print(i)
    if i == "b":
        print("This is something special!")

# Loop through a list of colors and print each color and its characters
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# Loop from 0 to 4 and print each number incremented by 1
for k in range(5):
    print(k + 1)

# Loop from 1 to 20000 and print each number
for k in range(1, 20001):
    print(k)

# Loop from 1 to 11 with a step of 3 and print each number
for k in range(1, 12, 3):
    print(k)

# While loop that continues until the user inputs a number greater than 38
i = int(input("Enter the number: "))
print(i)
while i <= 38:
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")

# While loop that counts down from 5 to 1 and then prints a message
count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("I am inside else")

# For loop that skips the iteration when i is 10
for i in range(12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)

# Infinite while loop that breaks when i is a multiple of 100
i = 0
while True:
    print(i)
    i += 1
    if i % 100 == 0:
        break

# Do-while loop example using a while loop with a break condition
i = 0
while True:
    print("Do-while loop iteration:", i)
    i += 1
    if i >= 5:
        break
