class Student:

    School_Name = 'Dayananda Sagar' #it is better to take class variable 
                                    #in capital letters
    def __init__(self,name,gender,age,e_marks,m_marks):
        self.name = name
        self.age = age
        self.gender = gender
        self.e_marks = e_marks
        self.m_marks = m_marks

    def totalMarks(self):
        
        return self.e_marks + self.m_marks


    def perSonalInfo(self):
        print(self.name,self.gender,self.age,Student.School_Name,)


student1 = Student('Raju','Male',19,22,23)
#student1.e_marks = 32 #It works when variables are not private
#print(student1.School_Name)#U can access common data with class name or with 
#print(Student.School_Name)   #object
student1.perSonalInfo()             
tot_marks = student1.totalMarks()
print(f'''Total marks of {student1.name} is {student1.e_marks}
                      +{student1.m_marks}
                      ={tot_marks}''','\n'*2)


student2 = Student('Rani','Female',18,24,23.5)
#print(Student.School_Name)
student2.perSonalInfo()
#student2.e_marks = 100 #u can modify when data is not private
tot_marks = student2.totalMarks()
print(f'''Total marks of {student2.name} is {student2.e_marks}  
                      +{student2.m_marks}
                      ={tot_marks}''','\n',Student.School_Name,'\n'*2)#u can 

                                                        #access common data from
student3 = Student('Daksh','Male',18,25,25)             #anywhere
student3.perSonalInfo()
tot_marks = student3.totalMarks()
print(f'''Total marks of {student3.name} is {student3.e_marks}  
                       +{student3.m_marks}
                       ={tot_marks}''','\n'*2)


student2 = Student('Rani','Female',18,24,23.5)
student2.perSonalInfo()
tot_marks = student2.totalMarks()
print(f'''Total marks of {student2.name} is {student2.e_marks}  
                      +{student2.m_marks}
                      ={tot_marks}''','\n'*2)
