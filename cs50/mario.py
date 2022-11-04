
def main():
    height = get_height()
    for i in range(height):
        print("#")



def get_height():
    while True:
        try:            #tratamento de erro
            n = int(input("Height? "))
            if n > 0:
                break
        except ValueError:
            print("It's not an integer")
    return n

if __name__ == "__main__":
    main()