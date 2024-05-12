numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
roman = ['i','iv','v','ix','x','xl','l','xc','c','cd','d','cm','m']
num = int(input('Enter the Decimal number: ')) # 120

for i in numbers[-1::-1]: #start from biggest val #20
    t = num // i  # 120 //m-->100 donot divid so....120//c(100)= 1, 20//10=2
    idx = numbers.index(i) # index of 100 = 8,index of 10 = 6
    print(roman[idx] * t,end = '') #index 8 in roman-->c*1(t=1)=c 
                                    #index 6 in roman = x*2(t=2)=xx
    num = num % i    #120%100 = 20  20%10=0 


'''numbers = [1,4,5,9,10]
roman = ['i','iv','v','ix','x']
num = int(input('Enter the number: '))

for i in numbers[-1::-1]:
    t = num // i
    idx = numbers.index(i)
    print(roman[idx] * t,end='')
    num = num % i'''
