#organizar os nomes, caso os usuarios digitem ,
import re           #importar a library para regular expressions

name = input("What's your name?" ).strip()
if matches := re.search(r"^(.+), *(.+)$", name):          # usar () para capturar  " *" = 0 ou 1 espaço         := assign a value e ask the boolean question
    name = matches.group(2) + " " + matches.group(1)     # executa se tiver uma virgula
print(f"hello, {name}")





"""
if "," in name:
    last, first = name.split(", ?")          # se tiver uma virgula, separa em duas variaveis e na hora de printar, coloca o nome primeiro
    name = f"{first} {last}"
print(f"hello, {name}")
"""