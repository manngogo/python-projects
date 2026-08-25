class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = int(account_id)
        self.account_type = account_type
        self.pin = int(pin)
        self.balance = float(balance)
    def deposit(self):
        print(f'Your current balance is... ${self.balance:,.2f}')
        print('Would you like to deposit money into your account?:')
        print('1. Yes')
        print('2. No')
        depositquestion = int(input('What would you like to do? 1. yes, 2. no: '))
        if depositquestion == 1:
            depositmoney = float(input('How much would you like to deposit?: '))
            self.balance += depositmoney
            print(f'Your new balance is... ${self.balance:,.2f}!')
            transactions = int(input('Would you like any other transactions? 1. yes, 2. no: '))
            if transactions == 1:
                welcome(self)
            elif transactions == 2:
                print('Thank you for your patronage!')
                print('Have a good day!')
            else:
                print('Error. Please try again later.')
                welcome(self)
        elif depositquestion == 2:
            print('No deposit made.')
            welcome(self)
    def withdraw(self):
        print(f'Your current balance is... ${self.balance:,.2f}')
        print('Would you like to withdraw?')
        print('1. Yes')
        print('2. No')
        withdrawquestion = int(input('What would you like to do?'))
        if withdrawquestion == 1:
            byemoney = float(input('How much would you like to withdraw?: '))
            if 0 <= byemoney <= self.balance:
                self.balance -= byemoney
                print('Withdrawing...')
                print('!')
                print('Thank you for your continued patronage.')
                print(f'Your current balance is... ${self.balance:,.2f}!')
                print('Would you like any other transactions?')
                print('1. Yes')
                print('2. No')
                byemoney1 = int(input('Would you like any other transactions?: '))
                if byemoney1 == 1:
                    welcome(self)
                elif byemoney1 == 2:
                    print('Thank you for your continued patronage!')
                    print('Have a good day!')
                else:
                    print('Error. Please try again later...')
                    welcome(self)
            else:
                print('This amount exceeds your current balance or is invalid.')
                self.withdraw()
        elif withdrawquestion == 2:
            print('No withdrawal made.')
            welcome(self)
    def display_balance(self):
        print(f'Your current balance is... ${self.balance:,.2f}!')
    def create_account(self):
        print('Creating account...')
        print('!')
        print(f'Account created for {self.first_name} {self.last_name}!')
        print(f'Your account ID is... {self.account_id}')
        print(f'Your account type is... {self.account_type}')
        print(f'Your PIN is... {self.pin}')
        print(f'Your current balance is... ${self.balance:,.2f}!')
def more_transactions(account):
    print('Would you like more transactions?')
    print('1. Yes')
    print('2. No')
    moretransactions = int(input('Would you like more transactions?'))
    if moretransactions == 1:
        welcome(account)
    elif moretransactions == 2:
        print('Thank you for your patronage!')
    else:
        print('Error. Please try again later...')
        welcome(account)

def creating_account():
    print('Please enter your account information.')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    account_id = input('Account ID: ')
    account_type = input('Account type: ')
    pin = input('PIN: ')
    balance = input('Starting balance: ')
    account = BankAccount(first_name, last_name, account_id, account_type, pin, balance)
    account.create_account()
    return account

def welcome(account):
    print('Hello!')
    print('Here are some things you can do at this ATM...')
    print('1. Display balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Create account')
    print('5. Exit')
    welcomequestion = int(input('What would you like to do?: '))
    if welcomequestion == 1:
        account.display_balance()
        more_transactions(account)
    elif welcomequestion == 2:
        account.deposit()
    elif welcomequestion == 3:
        account.withdraw()
    elif welcomequestion == 4:
        new_account = creating_account()
        welcome(new_account)
    elif welcomequestion == 5:
        print('Thank you for your patronage!')
        print('Come back next time!')
    else:
        print('Error. Restart and try again!')
        welcome(account)


oda = BankAccount('Nobunaga', 'Oda', 123456789, 'Checkings', 1582, 400000000)

welcome(oda)