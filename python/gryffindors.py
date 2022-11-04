students = ["Hermione", "Harry", "Ron"]


gryffindors = {student: "Gryffindor" for student in students}       # cria um dicionario



"""
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
______________

gryffindors = []

for student in students:            #cria uma lista de objetos em um dicionario
    gryffindors.append({"name": student, "house": "Gryffindor"})
"""


print(gryffindors)