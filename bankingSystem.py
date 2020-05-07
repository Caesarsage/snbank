import random
import json

print('WELCOME TO THE PYTHON BANKING FILES SYSTEM')
choice = input('Type in Your Preference:\n Login \n Close App \n')

def user_details():
    if choice.lower()=='login':
        username = input('Enter Your Username:\n')
        password = input('Enter Your Password: \n')
        #compare details
        with open('staff.txt', 'r') as myfile:
            user_data = myfile.read()
            data = json.loads(user_data)
            for user in user_data:
                if user['username'] == username and user['password'] == password:
                    user_board()
                else:
                    print('Incorrect User Details\n Try Again!!!')
    elif choice.lower() == 'close app':
        print('App Closed. \n Thanks for your time')
        exit()
    else:
        print('Unknown Input\n Try again!!!')
        user_details()


def user_board():
    print('WELCOME TO YOUR DASHBOARD!!!\n')
    choice2 = input('Input your operation as below \n Create New Bank Account \n Check Account Details \n Logout \n')
    if choice2.lower()=='create new bank account':
        #collect details
        acc_name = input('Enter your account name: \n ')
        openning_bal =input('Enter your Openning Balancen: \n')
        acc_type = input('Enter Your Account type: \n')
        acc_email = input('Enter Your Account Email \n')
        const = '209'
        acc_no_random = (const + random.randint(5,10)).__str__
        print('Your acc_no is '+ acc_no_random)
        #save to customer.txt file
        
    elif choice2.lower()=='check account details':
        input('Enter your account number')


def main():
    user_details()
    user_board()

main()