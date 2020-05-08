from datetime import date, datetime
import random
import os

print('WELCOME TO THE PYTHON BANKING FILES SYSTEM')


def user_details():
    choice = input('Type in Your Preference:\n Login \n Close App \n')
    login = True
    if choice.lower()=='login':
        while login == True:
            user_username = str(input('Enter Your Username:\n'))
            user_password = str(input('Enter Your Password: \n'))
        #compare details
            with open('staff.txt', 'r') as myfile:
                for user in myfile:
                    f = user.split(",")
                    username = str(f[0])
                    password = str(f[1])

                    if user_username.lower() == username.lower() and user_password == password:
                        print(f'hello {username}')
                        login = False
                        break  
                else:
                    print('Incorrect User Details\n Try Again!!!')
        

    elif choice.lower() == 'close app':
        print('App Closed. \n Thanks for your time\n See your next time and stay safe')
        exit()
    else:
        print('Unknown Input\n Try again!!!')
        user_details()

def user_board():
    print('WELCOME TO YOUR DASHBOARD!!!\n')
    createsession()
    choice2 = input('Input your operation as below \n Create New Bank Account \n Check Account Details \n Logout \n')
    if choice2.lower()=='create new bank account':    
        #collect details
        acc_name = input(str('Enter your account name: \n '))
        openning_bal =str(input('Enter your Openning Balance: \n'))
        acc_type = input(str('Enter Your Account type: \n'))
        acc_email = input(str('Enter Your Account Email \n'))
        acc_no_random = str(random.randint(1000000000,1999999999))
        print('Your acc_no is '+ acc_no_random)
        #save to customer.txt file
        with open('customer.txt', 'a') as file:
            file.write(acc_name)
            file.write(',')
            file.write(openning_bal)
            file.write(',')
            file.write(acc_type)
            file.write(',')
            file.write(acc_email)
            file.write(',')
            file.write(acc_no_random)
            file.write('\n')
        print('Details Save successfully')
        return user_board()
    elif choice2.lower()=='check account details':
        while  True:
            try:
                acc_num = input('Enter your account number\n')
                with open('customer.txt') as file:
                    for f in file:
                        field = f.split(",")
                        acc_name = str(field[0])
                        openning_bal = str(field[1])
                        acc_type = str(field[2])
                        acc_email = str(field[3])
                        acc_no_random = str(field[4])
                        last = len(acc_no_random) - 1
                        acc_no_random = acc_no_random[0:last]
                        if str(acc_num) == acc_no_random:
                            print(f'Your Account Name is {acc_name}')
                            print(f'Your Opening Balance is {openning_bal}')
                            print(f'Your Account Type is {acc_type}')
                            print(f'Your Account Email is {acc_email}')
                            file.close()
                            return user_board()
                    else:
                        print('Invalid Account Number')
            except ValueError:
                print('An Integer is required')
    elif choice2.lower()== 'logout':
        deletesession()
        print('Thanks for the session!!!')
        return user_details()


def createsession():
    today = date.today()
    with open('session.txt', 'w') as session:
        session.write(f'session started... \n {today}')
def deletesession():
    os.unlink('session.txt')
    print('Logged Out \n Session expired!!!')

def main():
    user_details()
    user_board()

main()