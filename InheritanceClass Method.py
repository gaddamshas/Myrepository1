class Student:

    #Common DATA--> can be used in Instance method as well as in Class method
    INSTITUTE_NAME = 'DAYANANDA SAGAR INSTITUTIONS' 
    STD_CNT = 0
    ALL_FEES = []
    def __init__(self,name,age,m1,m2,fee):

        #specifiC DATA
        self.name = name
        self.age = age
        self.e_marks = m1     
        self.m_marks = m2
        self.fee = fee
        Student.STD_CNT += 1
        Student.ALL_FEES.append(fee)

    #instance Method--> uses 'self'
    def info(self):

        print(self.name,self.age,self.e_marks,self.m_marks,self.fee,
              Student.INSTITUTE_NAME)

    #class Method--->U can access class variables/data only
    @classmethod #must include while creating class method
    def calcRevenue(cls): # 'cls'--->classname
        revenue = 0

        for amt in cls.ALL_FEES:
            revenue += amt

        return revenue


s1 = Student('Sachin',21,22,23,9500)
s1.info()

s2 = Student('Shashi',22,21,22.5,9700)
s2.info()

s3 = Student('Shrinidhi',22,23,23.5,9200)
s3.info()

s4 = Student('Shravan',23,24,224.5,9000)
s4.info()

print(f'Number of students are {Student.STD_CNT}')

print(Student.ALL_FEES)

rev = Student.calcRevenue()
print(f'Total revenue generated from this batch {rev}')
