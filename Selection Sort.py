
li = [11,1,12,14,3,5]

for i in range(0,len(li)):        # 0          
        min_val = min(li[i:])         #min(li[i:])=0
        idx = li.index(min_val)       # 1
        li[i],li[idx] = li[idx],li[i] # 0,1

print(li)
