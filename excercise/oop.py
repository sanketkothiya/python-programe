class employe:
    sk=1

    def __init__(self,name,age,profession):
        self.name=name
        self.age=age
        self.profession=profession

    def printdetails(self):

        return f" the owner name is {self.name} and age is {self.age}  and the profession is {self.profession}"


    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is a " + string)

sanket=employe('sanket',19,"computer_enginner")
rohan=employe("rohan",19,"michenical_engineer")
karan=employe.from_dash("sanketkothiya-23-manager")

# sanket.name = "koyhiya"
# sanket.age=19
# sanket.profession="computerengineer"

# print(karan.name)

# print(sanket.name)
# print(sanket.printdetails())
# print(sanket.__dict__)
# print(rohan.__dict__)

print(employe.printgood("sanket"))

