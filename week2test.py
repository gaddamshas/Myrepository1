string = ''' i
             am
             learning
             python
             from
             vcube
             vcube
             good
             for
             python '''
words = string.split()
#print(words)
word = []
wcnt = []
cnt = 0

for w in word:
    if w not in word:
        word.append(w)
        wcnt.append(1)
    else:
        idx = word.index(w)
        wcnt[idx] += 1
    cnt += 1

for i in wcnt:
    print(i)        
        
