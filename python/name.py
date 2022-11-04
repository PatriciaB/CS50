import sys

if len(sys.argv)<2:
    sys.exit("Too few arguments")           #sai da execucao

for arg in sys.argv[1:]:        # começa da posicao 1, nao zero, slices
    print("hello, my name is", arg)



"""


if len(sys.argv)<2:
    sys.exit("Too few arguments")           #sai da execucao
elif len(sys.argv)>2:
    sys.exit("Too many arguments")          #sai da execucao


print("hello, my name is", sys.argv[1])   #para chamar python name.py Patricia

--------------------------


if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])   #para chamar python name.py Patricia

___________________

try:
    print("hello, my name is", sys.argv[1])   #para chamar python name.py Patricia
except IndexError:
    print("Too few arguments")
    """