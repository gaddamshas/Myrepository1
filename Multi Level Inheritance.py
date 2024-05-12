class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        
    def info(self):
        
        print('Name:',self.name,'\n','Age:',self.age,end = ' ')

#ob1 = Person('IAS',29)
#ob1.info()
        
class Employee(Person):
    
    def __init__(self,name,age,eid,salary,):
        self.eid = eid
        self.salary = salary
        super().__init__(name,age)
        
    def eInfo(self):
        print('\n','ID:',self.eid,'\n','Salary:',self.salary,end =' ')
        
#ob2 = Employee('IAS',28,2,200000)
#ob2.info()
#ob2.eInfo()
        
class Manager(Employee):
    
    def __init__(self,name,age,eid,salary,rights):
        self.rights = rights
        super().__init__(name,age,eid,salary)
        
    def managerInfo(self):
        print('\nManager Special Rights:',self.rights)

p = Person('Shashi',27)

p.info()
print('\n'*3,'*'*20)

print('\n')

e = Employee('Trisha',27,1,125000)   
e.info()
e.eInfo()


print('\n'*3,'*'*20)

print('\n')

m = Manager('Daksh',45,2,250000,'Special Rights')
m.info()
m.eInfo()
m.managerInfo()
print('\n'*3,'*'*20)
