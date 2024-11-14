marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3])  # Negative index
print(marks[len(marks) - 3])  # Positive index
print(marks[5 - 3])  # Positive index
print(marks[2])  # Positive index

if 6 in marks:
    print("Yes")
else:
    print("No")

# Same thing applies for strings as well!
if "Ha" in "Harry":
    print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i * i for i in range(10)]
print(lst)
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
print(k)
l.extend(m)
print(l)

tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90  # This will raise an error because tuples are immutable
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])  # This will raise an IndexError

if 3421 in tup:
    print("Yes 342 is present in this tuple")

tup2 = tup[1:4]
print(tup2)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)
res = tuple1.index(3)
print('Index of first occurrence of 3 in tuple1 is:', res)
# res = tuple1.index(311)  # This will raise a ValueError
res = tuple1.index(3, 4, 8)
print('Index of 3 in tuple1 between positions 4 and 8 is:', res)
res = len(tuple1)
print('Length of tuple1 is:', res)