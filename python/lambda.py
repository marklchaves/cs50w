print("\nLambda\n")

people = [
    {"name": "Chewbacca", "house": "Sanggingan"},
    {"name": "Hope", "house": "Payogan"},
    {"name": "Millie", "house": "Payogan"}
]

"""
def f(person):
    return person["name"]
"""

# Lambda expression

#people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)
