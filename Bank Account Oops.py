class Bank_Account:

    def __init__(self):
        
        self.balance = 0

        print('**'*5,'''Hello! Welcome to SBI Cash Deposit and
              Withdrawal Machine''','**'*7)

    def deposit(self):

        amount = float(input('\nEnter amount to be Deposited: '))
        self.balance += amount
        print(f'\nDeposited amount {amount}')

    def withdraw(self):

        amount = float(input('\nEnter amount to be Withdrawn: '))

        if amount < self.balance:
            self.balance -= amount

            print(f'\nYou have Withdrawn {amount}')

        else:
            print('\nInsuffient Balance')

    def display(self):
        print(f'\n\nNet Available Balance = {self.balance}\n','*'*50)

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
