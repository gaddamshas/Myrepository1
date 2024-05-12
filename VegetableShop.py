veg = ['tomato', 'potato', 'onion', 'brinjal']
quantity = [10, 7, 12, 5]
price = [50, 40, 20, 45]

while True:

    item = input('Sir/Madam, what do you want? ')
    if item in veg:
        qunty = int(input('Sir/Madam, how many kgs you wat: '))

        idx = veg.index(item)

        if qunty <= quantity[idx]:
            total = qunty * price[idx]
            
            print(f'Sir/Madam, please pay {total} rupees, Thank you!')

        else:
            print('Sorry, Sir/Madam, we do not have those many kgs')

    else:
        print(f'Sorry, Sir/Madam, {item} is not available')

    ch = input('Do you want to close the shop? (yes/no): ')
    if ch == 'yes':
        print('Closing the shop....')
        break
        


    
