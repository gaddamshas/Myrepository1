a = [[10,20,30],[40,50,60],[70,80,90]]

print('Elements by row wise')
for i in a:
    print(i)
    
print('-'*20)

print('Elements in Matrix style')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()
 
