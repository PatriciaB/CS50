import csv          #importa uma biblioteca

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)           #usar DictReader se tiver cabeçalho
    for row in reader:
        students.append(row)



for student in sorted(students, key=lambda student: student["name"]):           #lambda é uma funcao sem nome
    print(f"{student['name']} is from {student['home']}  in {student['house']}")



"""
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})



for student in sorted(students, key=lambda student: student["name"]):           #lambda é uma funcao sem nome
    print(f"{student['name']} is from {student['home']} in {student['house']}")

    """




"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)



for student in sorted(students, key=lambda student: student["name"]):           #lambda é uma funcao sem nome
    print(f"{student['name']} is in {student['house']}")
    """