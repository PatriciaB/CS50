class Wizard:           #class onde estao as caracteristicas comuns às classes
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    def __str__(self):
        return f"{self.name}"

class Student(Wizard):          #herdar também as caracteristicas de Wizard
    def __init__(self, name, house):
        super().__init__(name)             #acessa a super class
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)             #acessa a super class
        self.subject = subject

    def __str__(self):
        return f"{self.name} from {self.subject}"
        

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dart Arts")

print(wizard)      # chama def __str__(self):
print(student)      # chama def __str__(self):
print(professor)      # chama def __str__(self):