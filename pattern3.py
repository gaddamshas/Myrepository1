s = input("Enter any string: ")
for i in range(0, len(s)):
    for k in range(0,len(s)):
        print(" ")
        for j in range(0, i):
            print(s[j], end=" ")
        
        print()
