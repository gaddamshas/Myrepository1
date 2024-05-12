

#f = open('E:\\samplefile.txt','w')# write mode-->overrides existing text

#f = open('E:\\samplefile.txt','a')# append mode-->append new text and existing
                                      #text will not be affected


#f.write('I am third line in a file\n')


#f = open('E:\\samplefile.txt','r')
#print(f)
#data = f.read() #will read all the text in a file
#print(data)

#data = f.read(11)#reads only first 11 characters
#print(data)

#line = f.readline()
#rint(line)

#line = f.readline()
#print(line)

#line = f.readline()
#print(line)

#lines = f.readlines()
#print(lines)

#f.seek(10)
#print(data)

#print(f.tell())


#f.close()

#Opening the file
'''with open("E:\\samplefile.txt",'r') as f:
    data = f.read()
    print(data)'''


'''data = open("E:\\samplefile.txt",'r')

print(data)

#data.close()'''


#With exceptions
'''try:
    data=open("E:\\samplefile.txt",'r')        
    print(data)
finally:
    data.close()'''

#Opening a new file and writing into it

#data1 = open('E:\File2.txt','w')
#data1.write('''kdhgaksuvbkvbsd kjhfdskj kdfhk kagk''')

#data1.close()
#data1 = open('E:\File2.txt','w')
#data1.write('''hawgh hfsj lafslh kfhsa ''')

#data1.close()'''

import os
os.rename('E:\\samplefile1.txt', 'E:\\samplefile.txt')
os.getcwd()
   
