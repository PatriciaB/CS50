import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("std4.csv", "a") as file:             #para adicionar linhas
    writer = csv.writer(file)
    writer.writerow([name, home])


"""
with open("std5.csv", "a") as file:             #para adicionar linhas  com cabeçalho
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})

"""