from sys import argv

if len(argv) == 2:
    print(f"hello, {argv[1]}")          #se digitar algo apos o nome do programa
else:
    print("hello, world")           #se nao digitar nada

"""
for arg in argv[1:]:     # ignora o nome do prog na hora de imprimir
    print(arg)

"""