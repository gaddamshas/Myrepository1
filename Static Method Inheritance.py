class Person:
    
    EXAMPLE = 'STATIC METHOD'
    def __init__(self,name,age):

        self.name = name
        self.age = age

    def info(self):
        print(self.name,'is',self.age,'year old')


    @classmethod
    def classInfo(cls):

        print('I am from class method')


    @staticmethod
    def isYoung(a):

        if a < 35:

            return 'Young'

        else:

            return 'Old'

#print(Person.EXAMPLE)
p1 = Person('Charan',16)

p1.info()

Person.classInfo()

print(p1.isYoung(35))
#print(p1.EXAMPLE)
