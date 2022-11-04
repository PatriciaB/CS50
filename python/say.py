import cowsay       #pip install cowsay
import sys          #usuario digita comando junto com o nome do arquivo a executar ... ex: python say.py Pat

if len(sys.argv) ==2:
    cowsay.cow("hello, " + sys.argv[1])
 #   cowsay.trex("hello, " + sys.argv[1])  #   aparece um T-rex