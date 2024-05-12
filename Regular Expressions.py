import re
s = '''i am Shashi i am learning python since 2022 pychan
     and python is beautiful language,Male Female
     and more Popular since 2012
     shsashi19yadav@gmail.com Male 
     shashi_19gaddam@gmail.com
     +917676487759
     9739770977
     7204252102 Male Female
     9632048449'''

#res = re.findall('\d{4}',s) #['20', '14', '20', '12']-->if {4} then ['2014', '2012']

#print(res)

#print(re.findall('\w',s)) #prints characters

#print(re.findall('\w+',s)) #prints group of characters--> words

#print(re.findall('[0-9]',s))#individual digits

#print(re.findall('[0-9]+',s))#group of digits

#print(re.findall('[A-Z][a-z]',s)) #['Sh']

#print(re.findall('[A-Z][a-z]+',s)) #['Shashi']

#print(re.findall('\d{10}',s)) #['7676487759', '9739770977', '7204252102', '9632048449']

#print(re.findall('[a-z0-9]+@[a-z]+\.com',s))

#print(re.findall('\+[0-9]+',s))

#res = re.findall('\d{10}',s)
#print(res)

#res = re.findall(('p....n'),s)
#print(res)

#print(re.findall('(Female)',s))


