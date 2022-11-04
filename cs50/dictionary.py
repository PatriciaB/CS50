words = set()  #hash table, dictionary

def check(word):
    if word.lower() in words:   # força em maiusculo
        return True
    else:
        return False



def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        word = line.rstrip()   #tirar a nova linha
        words.add(word)
    file.close()
    return True


def size():
    return len(words)

def unload():
    return True