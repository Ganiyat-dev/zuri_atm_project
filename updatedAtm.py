
import random

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def init():
    print("Welcome to Ghina ATMBank")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()

usersDatabase = [
    {'userName':'abdulmumeen', 'password':'123', 'balance':'0','accountNumber':'1234567890'}
]

def register():
    print("****** Register *******")
    newUser = {}
    newUser['userName'] = input("Enter your username \n")
    newUser['password'] = input("Create a password for yourself \n")

    newUser['accountNumber'] = generateAccountNumber()
    newUser['balance'] = 0
    usersDatabase.append(newUser)
    for user in usersDatabase:
        if user['userName'] == newUser['userName']:
            print("Your Account Has been created")
            print(" == ==== ====== ===== ===")
            print ("Your account number is {}".format(user['accountNumber']))
            login()

    else:
        print("Something went wrong, please try again")
        register()


def login():
    print("********* Login ***********")

    usernameFromUser = input("What is your username? \n")
    for user in usersDatabase:
        if(user['userName'] == usernameFromUser):
            password = input("Your password? \n")    

            if(password == user['password']):
                
                print('Welcome %s' % user['userName'])
                bankOperations(user['userName'])    
            
            
        else:
            print('Account Validation failed, please try again')
            login()


def bankOperations(user):
    
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) check balance (4) Logout (5) Exit \n"))

    if selectedOption == 1:
        depositOperation(user)

    elif selectedOption == 2:
        withdrawalOperation(user)
    
    elif selectedOption == 3:
        checkBalance()

    elif selectedOption == 4:
        logout()

    elif selectedOption == 5:
        exit()

    else:
        print("Invalid option selected")
        bankOperations(user)

def depositOperation(user):
    print("___Deposit Operations___")
    amount = input("Enter amount to deposit")
    for account in usersDatabase:
        if account['userName'] == user:
            account['balance'] += amount
            print('You deposited #{} and your balance is {}'.format(amount, account['balance']))
            bankOperations(user)

def withdrawalOperation(user):
    print('___Withdrawal Operation___')
    for account in usersDatabase:
        if account['userName'] == user:
            print('Your Balance: {}'.format(account['balance']))
            amount = input('Enter amount to withdraw')
            if account['balance'] < amount:
                print('Insufficient balance')
            else:
                account['balance'] -= amount
                print ('Your balance remains {}'.format(account['balance']))


def checkBalance(user):
    for account in usersDatabase:
        if account['userName'] == user:
            print('Your Balance: {}'.format(account['balance'])) 

def logout():
    login()


init()
