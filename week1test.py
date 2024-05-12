li = [2,3,-1,4,-1,6,10,5,-1,19,-1,1]
sort = []
for i in range(0,len(li)):
    min_val = min(li)
    #idx = li.index(min_val)
    #li[i],li[idx]=li[idx],li[i]
    sort.append(min_val)
    li.remove(min_val)
print(sort)

