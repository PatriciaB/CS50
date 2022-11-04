students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}               #dicionario


#print(students["Hermione"])    # olha para a chave (key) e imprime o que esta associado

for student in students:
    print(student, students[student], sep=", ")       #imprime a chave e o que esta associado a ele, (sep=", ") é usado para separar