def genExp():
    print('First')
    yield 1

    print('Second')
    yield 2

    print('Third')
    yield 3

    
    print('Fourth')
    yield 4

    print('Fifth')
    yield 5

for i in genExp():
    print(i)





            
