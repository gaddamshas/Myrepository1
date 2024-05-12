'''s = 'i am learning Python since 2022'

chars = []
chcnt = []

for ch in s:
    if ch in chars:          #if i in chars then stores indes in idx
        idx = chars.index(ch) 
        chcnt[idx] +=1 #index of already appended character count increases
    else:
        chars.append(ch) # if i not in chars then appends i to chars[]
        chcnt.append(1) #append one count at a time to chcnt[]
#print(chars)
#print(chcnt)

for item in zip(chars,chcnt): #zip() combine values from chars and counts 
    print(item)            #in organized manner'''

string = '12222311'

#s = str.upper(string)#it will convert lower case letters to upper case
#print(s)
chars = []
charcnt = []
cnt = 0
for ch in string:

    if ch not in chars:
        chars.append(ch)
        charcnt.append(1)

    else:
        idx = chars.index(ch) 
        charcnt[idx] += 1
        
    cnt += 1
#print('Total letters=',cnt,'\n')#print numbers of letters in the string
for item in zip(charcnt,chars): #it will zip letters and numbers times that 
    print(item)            #letter repeated in the string
    
