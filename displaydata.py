# code to display user activities 
# it accepts username and category as parameter
# it diplays all activities that belong the username
# it print error message when no activity is found
def displaydata(username,activity):
    activities_data = []
    get_activity_data = open('activities/log.txt', 'r').readlines()
    for my_activity in get_activity_data:
        activities_data.append(my_activity.split())
    counter = 0
    activity_count = 0
    activities_length = len(activities_data)    
    while counter < activities_length:
        if activities_data[counter][0] == username and activities_data[counter][1] == activity:
            activity_count += 1
            print(str(activity_count) + ". TIME: "+activities_data[counter][2]+" DISTANCE: "+activities_data[counter][3]+" HEARTBEAT: "+activities_data[counter][4])
        counter += 1
    if activity_count == 0:
        print("SORRY NO ACTIVITY WAS FOUND")