names = []              #empty list

for _ in range(3):  #3 times
    names.append(input("What's your name? "))


for name in sorted(names):      # colocar em ordem
    print(f"hello, {name}")