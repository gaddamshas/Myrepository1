
s = 'i am learning python'
alreadycounted = []
cnt = 0
for ch in s:
    if ch not in alreadycounted:
        cnt = s.count(ch)
        print(ch,cnt)
        alreadycounted.append(ch)



