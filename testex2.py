class Person:

    
    def __init__(self,firstname,lastname,age,sex):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def info(self):
        print(self.firstname,self.lastname,self.age,self.sex)



p1 = Person('Ravi','Raj',24,'M')
p1.info()
