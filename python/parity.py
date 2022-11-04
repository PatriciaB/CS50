def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


#define uma funcao, True e False precisa ser com a primeira letra maiuscula
def is_even(n):
    #return True if n % 2 ==0 else False
    return n % 2 == 0

main()