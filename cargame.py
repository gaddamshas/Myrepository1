start = 0
while True:
    print("**"*15)
    print("Plese select the option")
    print("1.Start")
    print("2.Stop")
    print("3.Exit")
    ch = int(input("Enter the option: "))
    if ch == 1:
        if start == False:
            print("Car started")
            start = True
        else:
            print("Car already started")
    if ch == 2:
        if start == True:
            print("Car stopped")
            start = False
        else:
            print("Car already stopped")
    if ch == 3:
        print("Exit")
        break
    else:
        if ch > 3:
            print("Invalid option")
    print("**"*15)
