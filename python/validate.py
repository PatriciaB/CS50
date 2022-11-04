#validar email do usuario
import re

email = input("What's your email? ").strip()      #tirar espaços em branco  .lower() transforma em minusculo

if re.search(r"^(\w|_|.|-)+@(\w+\.)?\w+\.(com|edu)$", email, re.IGNORECASE):       # $ significa o final, terminar com aquela expressao  -   \. quer dizer que quer um ponto   [^@] - exceoto @  \w - any word or number
    print("Valid")                  #(\w+\.)? pode estar ou nao
else:
    print("Invalid")






"""

username, domain = email.split("@")
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")



if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

"""