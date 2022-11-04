def main():
    yell("This", "is", "CS50")

def yell(*words):       #para aceitar mais de um argumento
    uppercased = [word.upper() for word in words]          #maiuscula               list comprehensions
    print(*uppercased)


"""
def yell(*words):       #para aceitar mais de um argumento
    uppercased = map(str.upper, words)          #maiuscula, passando a referencia da funcao str.upper
    print(*uppercased)
"""

if __name__ == "__main__":
    main()