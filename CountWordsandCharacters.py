s = 'i am learning python i am learning python'

key = []
cnt = []

words = s.split() #splits the string into words 
print(words,'\n')

for word in words: # i, am
    if word in key: # 
        idx = key.index(word) # 0

        cnt[idx] += len(word) #0+1(len of i = 1)

    else:
        key.append(word) # if not in words[] then add i to words[]
        cnt.append(len(word)) #length of word i=1,am=2,python=6...

#print(key)
#print(cnt)

for i in zip(key,cnt): #combiles key elements and count elements
    print(i,'\n')
