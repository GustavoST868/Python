class Pessoa:

    def __init__(self,name,age,address,wheigth):
        self.name = name
        self.age = age
        self.address = address
        self.wheigth = wheigth

    def PrintName(self):
        print(f"\n\nName = {self.name}")

    def PrintAge(self):
        print(f"Age = {self.age}")
    
    def PrintAddress(self):
        print(f"Address = {self.address}")

    def PrintWheight(self):
        print(f"Wheight = {self.wheigth}\n\n")

    def PrintAll(self):
        self.PrintName()
        self.PrintAge()
        self.PrintAddress()
        self.PrintWheight()

    


     