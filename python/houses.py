students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Padma", "house": "Ravenclaw"},
]



houses = set()          #a class
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)




"""
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)

"""