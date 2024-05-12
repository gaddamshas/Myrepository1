def evennumber(start,end):
    output = []
    for i in range(start,end+1):
       
        if i % 2 == 1:
            
            output.append(i)
           
           
            
    return output
    


print(evennumber(1,20))
#print(res)


res = evennumber(20,40)
print(res)
print('After second call')



