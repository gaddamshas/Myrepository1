#RotationRight
li = [1,2,3,4,5]
output = []
num = int(input('Enter the index number from which you want start rotation: '))
if num in li:
    idx = li.index(num)
    output.extend(li[idx + 1:])
    output.extend(li[:idx + 1])
else:
    print('Rotation not possible')
print(output)
    
