def decfun(item):


    def itemfun():
        
        item()
        
        items = input()
        it = [Onion,tomato,carrot,capsicum,potato]
        qty = [15,10,5,7,20]
        pri = [25,20,40,35,30]

        reitem = input('What do you want sir?:')
        if reitem in it:
            
            
            reqty = int(input('how many kgs you want?'))
            if reqty <= qty:
                print('Sir please pay',)

        else:
            print('Sorry sir, item not availble')
        

        print('Your total bill is_____rupees')
       
        print('Thank You! Visit again')

    return itemfun
        

    
    
@decfun


def billingfun():
    print('Please pay the bill for the items: ')
    
billingfun()
