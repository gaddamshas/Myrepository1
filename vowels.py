from os import remove


s = 'abcdeaofgheeiiomjne'
v = 'aeiouAEIOU'
cnt = 0
vo = []
for c in s:
    #print(c)
    #print(len(v))
    if c in v:
        #print(c)
        cnt += 1
        vo.append(c)
        if len(vo) >= 2:
            print(vo)
    else:
         if len(vo)< 2 and c not in v:
            break
            
print(vo)
        #if cnt >= 2:
            #print