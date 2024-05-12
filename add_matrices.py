mat1 = [[10,20,30],[40,50,60],[70,80,90]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]
#n1 = int(input('Enter number of elements of list1: '))
#n2 = int(input('Enter number of elements of list2: '))
#mat1 = []
#mat2 = []
#print('\nEnter list1 Elements\n')
#for a in range(0,n1):
    #m1 = int(input(f'Enter {a}th element: '))
    #mat1.append(m1)
#print(mat1)
#print('\nEnter list2 Elements\n')
#for b in range(0, n2):
    #m2 = int(input(f'Enter {b}th element'))
    #mat2.append(m2)
#print(mat2)
#result=[0]
result = [[0,0,0],[0,0,0],[0,0,0]]
    
for i in range(len(mat1)):
    for j in range(len(mat2)):
        result[i][j] = mat1[i][j] + mat2[i][j]

print('The addition of matrices is\n')
for r in result:
    print(r)
