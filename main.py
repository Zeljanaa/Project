import os.path
from save_activity import savenewrecord
from register_user import register
from loggedIn_session import logged_session

def login():
    # get user login information from console
    username = input('Enter username: ')
    password = input('Enter password: ')

    # read through each line of data stored in log file(register.txt)
    get_data = open('register.txt', 'r').readlines()
    
    # loop through each line appending each line in a list
    users_data = []
    for user in get_data:
        users_data.append(user.split())
        
    # get length of the created list
    total_user = len(users_data)
    
    # authenticate username and password
    increment = 0
    login_success = 0
    while increment < total_user:
        usernames = users_data[increment][0]
        passwords = users_data[increment][1]
        if username == usernames and password == passwords:
            login_success = 1
        increment += 1

    if login_success == 1:
        # invoke logged_session function because login was successful, passing an argument of logged in user
        logged_session(username);
    else:
        print('invalid username & password')


def startprogram():
    # Ensure that we have a file named register.txt to store user information
    if not os.path.exists('register.txt'):
        file = open('register.txt', 'w')
        file.close()
    # ask if user already has an account
    question = input('Do you have an account? yes | no : ')
    if question == 'yes':
        # user has a account so we invoke login function
        login()
    else:
        # user does no have account, so we call register function, then login function follows
        register()
        login()
# this is the entrypoint of the program
startprogram()
