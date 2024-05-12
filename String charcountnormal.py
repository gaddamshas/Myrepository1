'''s = 'i am learning python'
alreadycounted = []
cnt = 0
for ch in s:
    if ch not in alreadycounted:
        cnt = s.count(ch)
        print(ch,cnt)
        alreadycounted.append(ch)'''


string = 'welcome to department of computer science'

alreadycounted = []
cnt = 0
for ch in string:

    if ch not in alreadycounted:
        cnt = string.count(ch)
        print(ch,cnt)

        alreadycounted.append(ch)

    


