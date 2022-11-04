def main():
    x = get_int("What's x? ")
    print(f"x is {x}")              #outra forma de representar o print. nao esquecer f



def get_int(prompt):
    while True:                 #loop infinito até o break
        try:
            return int(input(prompt))           #it will break and return the value
        except ValueError:
            pass                #nao faz nada, continua o loop

main()







"""
def main():
    x = get_int()
    print(f"x is {x}")              #outra forma de representar o print. nao esquecer f



def get_int():
    while True:                 #loop infinito até o break
        try:
            x = int(input("Digite x: "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
"""