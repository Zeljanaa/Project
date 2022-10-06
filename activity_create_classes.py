#function to save new activity
from save_activity import savenewrecord

# class to instantiates any create activity object with username, and the activity name
class GeneralActivity(object):
    def __init__(self,username,activity):
        self.username=username
        self.activity=activity

# This class inherits the Generals activity class and initializes it when an object type Activity is created
# has function save to save a new activity
# save calls savenewrecord function save a new activity     
class Activity(GeneralActivity):
  def __init__(self,username,activity):
    super().__init__(username, activity)
  def save(self,time,distance,heartbeat):
    savenewrecord(self.username,self.activity,time,distance,heartbeat)