
# This code registers a new user
def register():
    # get first name from console
    first_name = input('Enter First Name: ')
    # get last name from console
    last_name = input('Enter Last Name: ')
    # get age name from console
    age = input('Enter Age: ')
    # get gender from console
    gender = input('Enter Gender: ')
    # get user register data from console
    username = input('Enter username: ')
    # ensure that username does no exist
    if username in open('register.txt', 'r').read():
        print('Username already exists')
        exit()
    password = input('Enter password: ')
    c_password = input('Enter confirm password: ')
    # Ensure that the password does no exist
    if password != c_password:
        print('Sorry password not match')
        exit()
    sport = ''
    print('Select a Sport: ')
    print('1. running: ')
    print('2. cycling: ')
    print('3. swimming ')
    option = input("> ")
    if option == "1":
        sport = 'running'
    elif option == "2":
        sport = 'cycling'
    elif option == "3":
        sport = 'swimming'
    else:
        print('invalid choice!!Try again!!')
        print()
        print()
        exit()
    # save user data to log file (register.txt)
    handle = open('register.txt', 'a')
    handle.write(username)
    handle.write(' ')
    handle.write(password)
    handle.write(' ')
    handle.write(first_name)
    handle.write(' ')
    handle.write(last_name)
    handle.write(' ')
    handle.write(age)
    handle.write(' ')
    handle.write(gender)
    handle.write(' ')
    handle.write(sport)
    handle.write('\n')
    handle.close()
    print('User was successfully registered')
    print('')
    print('')
    print('')
    print('YOU CAN NOW LOGIN')