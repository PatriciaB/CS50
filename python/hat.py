import random


class Hat:
    houses = ["Griffindor", "Huffleupuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))    #randomicamente, importar a  biblioteca



Hat.sort("Harry")