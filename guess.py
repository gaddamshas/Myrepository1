import random
#cnt = 1
while True:
    fix = random.randint(1, 5)
    print(fix)
    cnt = 1
    print("You have ONLY THREE guesses")
    while(cnt <= 3):
        guess = int(input("Enter the number: "))
        if(fix == guess):
            print("You won the game")
            break
        else:
            print("wrong guess")
        cnt += 1
    print("Do you want to continue?")
    print("Yes or No")
    userop = str(input())
    #print("Yes or No")
    #userop = str(input("do you want to continue Yes or No?: "))     
    if(userop == 'no'):
        if (fix != guess):
            print('You lost the game')
        break
print("game over")
