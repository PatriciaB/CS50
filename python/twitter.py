#salvar o usuario do twitter em uma variavel, considerando as diferentes formas que o usuario por digitar a URL

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

"""
username = re.sub(r"^(https?://)?(www.\)?twitter\.com/", "", url)            # . significa qualquer caracter, usar o caracter de escape e colocar o acento circunflexo no inicio
print(f"username: {username}")                                               # para deixar algo opcional, agrupar com () e colocar ? após



username = url.replace("https://twitter.com/", "")
print(f"username: {username}")


"""