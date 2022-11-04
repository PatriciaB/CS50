def main():
    height = int(input("Height:" ))
    pyramid(height)


def pyramid(n):
    for i in range(n):
#        print(i, end="")
#        print("#" * i)
         print("#" * (i+1))          #para adicionar

if __name__ == "__main__":
    main()