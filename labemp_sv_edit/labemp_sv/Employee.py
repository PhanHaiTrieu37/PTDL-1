import code


class Employee:
    def __init__(self,code,name,age,salary):
        self.code = code
        self.name = name
        self.age = age
        self.salary = salary
    def income(self):
        result = 0.9*12*self.salary
        return result

    def getCode(self):
        return self.code

    def setCode(self, code):
        if (self.code == None ):
            self.code = "khong xac dinh"
        else:
            self.code = code
  
    def getName(self):
        return self.name

    def setName(self, name):
        if (self.name == None ):
            self.name = "khong xac dinh"
        else:
            self.name = name
            
    def getAge(self):
        return self.age

    def setAge(self, age):
        if (self.age <= 0 ):
            self.age = 1
        else:
            self.age = age

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        if (self.salary <= 0 ):
            self.salary = 1
        else:
            self.salary = salary

    def increaseSalary(self,amount):
        if amount > 0:
            self.salary = self.salary+ amount

    def diminishSalary(self,amount):
        if amount > 0:
            self.salary = self.salary - amount
    
    def display(self):
        print(f'code: {self.code}, name: {self.name}, age: {self.age}, salary: {self.salary}, income: {self.income()}\n')