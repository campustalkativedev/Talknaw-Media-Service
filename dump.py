from datetime import datetime


# init 
# self
# inheritance 
#iterables


class School:
    def __init__(self, name, creation_date):
        self.name = name
        self.creation_date = creation_date
        #        # Constructor
        self.c = 10
        

    def classroom1(self):
        print(self.c)

        self.c = 1000

        print(self.c)
        print(self.name)
        self.name = "XYZ"
        return "Classroom 1"

    def classroom2(self):
        self.c = 300

        print(self.c)
        print(self.name)
        return "Classroom 2"


school1 = School(name="ABC", creation_date=datetime.utcnow()) #self
school2 = School(name="MNO", creation_date=datetime.utcnow()) #self


school1.classroom1()

school2.classroom2()


class Univerisity(School):

    def classroom1(self):
        original = super().classroom1()

        return "Classroom 2"
    ...


uni = Univerisity(name="XYZ", creation_date=datetime.utcnow())

uni.classroom1()


class Calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

calc = Calculator(num1=num1, num2=num2)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())