students = [                #dicionario
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}          #Nome: significa nada
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")

"""    if student["name"] == "Ron":
        print(student["name"], student["house"], student["patronus"], sep = ", ")
"""