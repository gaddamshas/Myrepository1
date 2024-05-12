#Print the numbers in an order that is closer to the given number
li = [33,49,65,50,63,90]

x = 50
output = []
out1 = []

for val in li: #33, 49, 65, 50, 63, 90
    #print(val)

    if x > val: 
        output.append(x - val) #50-33=17,50-49=1

    else:
        output.append(val - x) #65-50=15, 50-50=0, 63-50=13, 90-50=40

    #print(output)           #[17,1,15,0,13,40]

print(output)
#leng = len(output)             #[17,1,15,0,13,40]

for i in range(0,len(output)): #0(index)=17(value),1=1, 2=15,3=0,4=13,5=40
    #print(i)
    min_val = min(output) #0,
    #print(min_val)
    idx = output.index(min_val)#0->3
    #print(idx)
    out1.append(li[idx])#out1=[50,]
    #print(out1)
    output.remove(min_val)
    #print(output)
    li.remove(li[idx])
    #print(li)

print(out1)




