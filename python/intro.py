# name = input("Name: ")
# print(f"Hello, {name}")

"""
n = int(input("Number: "))

if n >0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
"""

# List of names

print("\nList of names\n")

names = ["Chewie", "Hope", "Mille"]

print("\n")
print(f"names[0] = {names[0]}")

#names.append("Bobby")

names.sort()

print("\n")
print(names)

# Set

print("\nSet\n")

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

s.add(3)

print("\n")
print(s)

s.remove(2)

print("\n")
print(s)

print(f"\nThe set has {len(s)} elements.\n")

# Loops

print("\nLoops\n")

max_num = -99999

print("\nLoop through a list of numbers.\n")

for i in [0, 1, 2, 3, 4, -2, 3, 10, 69, 21, 1, -20]:
    print(i)
    if i > max_num:
        max_num = i

print(f"\nmax_num = {max_num}\n")    

name = "Chewbacca"

print("\nLoop through characters in a string.\n")

for char in name:
    print(char)
