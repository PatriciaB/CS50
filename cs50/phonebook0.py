import csv

name = input("Name: ")
number = input("Number: ")

with open("phonebook.csv", "a") as file:         #nao precisa fechar
    writer = csv.writer(file)
    writer.writerow([name, number])           # print a list



