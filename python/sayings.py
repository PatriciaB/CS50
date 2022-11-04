def main():
    hello("world")
    goodbye("word")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":          #- run by command line, se for usada uma função, nao chama o main
    main()