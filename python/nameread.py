names = []

with open("names.txt") as file:        #ler o arquivo
    for line in file:
        names.append(line.rstrip())             #colocar em uma lista na memoria, striping off, tirar os enters

for name in sorted(names):          #for name in sorted(names, reverse=True):     faz em ordem decrescente
    print(f"hello, {name}")






"""
with open("names.txt") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip())
"""