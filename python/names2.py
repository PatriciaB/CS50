name = input("What's your name? ")

with open("names.txt", "a") as file:   #nome do arquivo, "w" significa escrever, "a" é alterar
    file.write(f"{name}\n")         #nova linha
