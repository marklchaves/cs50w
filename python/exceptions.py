import sys

print("\nExceptions\n")

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("\nError: Cannot divide strings.")
    print("\nPlease enter a number.\n")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("\nError: Cannot divide by 0.\n")
    sys.exit(1)

print(f"\n{x} / {y} = {result}\n")
