import sys

from sayings import hello       #importa uma funcao que nós criamos


if len(sys.argv) ==2:
    hello(sys.argv[1])