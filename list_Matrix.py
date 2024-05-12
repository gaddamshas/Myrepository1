#Nested List

list1 = [[10,20,30],[40,50,60],[70,80,90]]


#Prints in row wise
for n in list1:
    print(n)


for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j], end = ' ')
    print()

print()


l = ['a',10,'b',20,'c',30,'d',40,'e',50,'f',60,'g',70,'h',80,'i',90]
dict(l)
