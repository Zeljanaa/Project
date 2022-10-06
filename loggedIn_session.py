# function to display activities
from displaydata import displaydata
# function to create a new activity
from activity_create_classes import GeneralActivity, Activity
def logged_session(username):
    # Account login welcome message
    print()
    print()
    print('Welcome ' + username)
    while True:
        # display acount activities that user can do and allow him to select an activity to do
        print("AVAILABLE OPTIONS:")
        print("1. display all categories")
        print("2. display my activities under a specific category")
        print("3. register new activity")
        print("4. exit")
        option = input("SELECT AN OPTION> ")
        print()
        print()
        if option == "1":
            # display a list of available categories
            while True:
                print("BELOW IS A LIST OF CATEGORIES")
                print("running")
                print("cyling")
                print("swimming")
                userin = input("press any key to go back>")
                print()
                print()
                break
        elif option == "2":
            # display a list of available categories allowing user to choose
            while True:
                print("BELOW IS A LIST OF CATEGORIES")
                print("1. running")
                print("2. cyling")
                print("3. swimming")
                print("4. back")
                option = input("SELECT CATEGORY TO VIEW ITS ACTIVITIES> ")
                if option == "1":
                    displaydata(username,"running")
                if option == "2":
                    displaydata(username,'cycling')
                if option == "3":
                    displaydata(username,'swimming')
                if option == "4":
                    print()
                    print()
                    break
                print()
                print()
        elif option == "3":
            # display a list of available categories allowing user to choose befor registering
            while True:
                print('AVAILABALE ACTIVITIES')
                print("1. running")
                print("2. cycling")
                print("3. swimming")
                print("4. back")
                option = input("SELECT ACTIVITY TO REGISTER> ")
                if option == "1":
                    # get activity details for running
                    activity = "running"
                    time = input("enter activity time> ")
                    distance = input("enter activity distance> ")
                    heartbeat = input("enter activity heartbeat> ")
                    activity_obj = Activity(username,activity)
                    activity_obj.save(time,distance,heartbeat)
                    print("ACTIVITY REGISTERED SUCCESSFULLY")
                    print()
                    print()
                elif option == "2":
                    # get activity details for cycling
                    activity = "cycling"
                    time = input("enter activity time> ")
                    distance = input("enter activity distance> ")
                    heartbeat = input("enter activity heartbeat> ")
                    activity_obj = Activity(username,activity)
                    activity_obj.save(time,distance,heartbeat)
                    print("ACTIVITY REGISTERED SUCCESSFULLY")
                    print()
                    print()
                elif option == "3":
                    # get activity details for swimming
                    activity = "swimming"
                    time = input("enter activity time> ")
                    distance = input("enter activity distance> ")
                    heartbeat = input("enter activity heartbeat> ")
                    activity_obj = Activity(username,activity)
                    activity_obj.save(time,distance,heartbeat)
                    print("ACTIVITY REGISTERED SUCCESSFULLY")
                    print()
                    print()
                elif option == "4":
                    # go to the previous menu
                    break        
        elif option == "4":
            print()
            print()
            # go to the previous menu
            break
        else:
            # show error message for invalid input
            print(option + " is not an option")
            print()
            print()