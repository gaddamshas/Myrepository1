div=1
cnt=0

num=int(input("Enter the number: "))

if(num > 1):
    if(num > 2 and num % 2 == 0):
        print(f'{num} is not a Prime Number')

    else:
        while(div <= num):
            if(num % div) == 0:
                cnt += 1  
            div += 1

            if cnt > 2:
                print(f'{num} is not a Prime Number')
                break
        else:
            print(f'{num} is not a Prime Number')
       

        
