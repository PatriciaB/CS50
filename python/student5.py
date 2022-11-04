class Student:    #nome da class, colocar com primeira maiuscula
    def __init__(self, name, house):            #sempre usar o self
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):  #get and setter trabalham juntos
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name



    #getter
    @property
    def house(self):
        return self._house

    #setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house


    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)      #constructor



def main():
    student = Student.get()
    print(student)      # chama def __str__(self):



if __name__ == "__main__":
    main()


