#RotateLeft
li = [1,2,3,4,5]
output = []
num = int(input('Enter the index of the list, from where you want to rotate: '))
if num in li:
    idx = li.index(num)
    output.extend(li[idx-1::-1])
    output.extend(li[-1:(idx-len(li)-1):-1])
else:
    print('Rotation not possible')
print(output)
