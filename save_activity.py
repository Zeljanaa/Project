import os
# This code saves the activity details details of newly registered activity
def savenewrecord(username,activity,time,distance,heartbeat):
    filename = 'activities/log.txt'
    # ensure that activity log file exists
    if not os.path.exists(filename):
        file = open(filename, 'w')
        file.close()
    handle = open(filename, 'a')
    handle.write(username)
    handle.write(' ')
    handle.write(activity)
    handle.write(' ')
    handle.write(time)
    handle.write(' ')
    handle.write(distance)
    handle.write(' ')
    handle.write(heartbeat)
    handle.write('\n')
    handle.close()
    return True