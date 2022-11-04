class Student:    #nome da class, colocar com primeira maiuscula
    def __init__(self, name, house, patronus):            #sempre usar o self
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):        #at least one object
        match self.patronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🦦"
            case _:
                return "🤡"


def main():
    student = get_student()
    print(student)      # chama def __str__(self):
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)      #constructor



if __name__ == "__main__":
    main()



"""
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]            #com [] retorna uma lista, que pode ser alterada


def get_student():
    name = input("Name: ")      #dictionary
    house = input("House: ")
    return {"name" : name, "house" : house}
"""