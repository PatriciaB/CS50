with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")                #separar usando o argumento ,   se souber que sao só duas colunas....
        print(f"{name} is in {house}")

        """
        row = line.rstrip().split(",")                #separar usando o argumento ,
        print(f"{row[0]} is in {row[1]}")

        """