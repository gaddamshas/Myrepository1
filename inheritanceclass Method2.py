class Student:
    ALL_MARKS = []
    STD_CNT = 0
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        Student.ALL_MARKS.append(marks)
        Student.STD_CNT += 1

    def info(self):
        print(self.name,self.age,self.marks)


    @classmethod
    def calcMarks(cls):
        
            mrk = 0
            for mrks in cls.ALL_MARKS:
                mrk += mrks 

            return mrk


            
s1 = Student('Ravi',22,97)
s1.info()

s2 = Student('Ram',20,88)
s2.info()

s3 = Student('Shashi',21,99)
s3.info()


s4 = Student('Shah',22,98)
s4.info()

print(f'Number of Students are {Student.STD_CNT}')

tot = Student.calcMarks()
print(f'Total Marks {tot}')



