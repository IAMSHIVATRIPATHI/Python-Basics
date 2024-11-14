# identify the time zone and greet

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
minute = time.strftime('%M')
second = time.strftime('%S')

print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")

if 5 <= hour < 12:
    print("Good morning!")
elif 12 <= hour < 17:
    print("Good afternoon!")
elif 17 <= hour < 21:
    print("Good evening!")
else:
    print("Good night!")