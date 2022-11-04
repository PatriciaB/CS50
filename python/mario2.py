def main():
    print_square(3)

"""
def print_square(size):
    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):

            #print brick without the end of the row
            print("#", end="")

        #print one black new row
        print()

"""
def print_square(size):
    for i in range(size):
        print("#" * size)

main()