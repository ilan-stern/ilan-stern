import json
""" 
Day Planner
    V1
    - Before your day input what activities you will part take in with times (locations in later version)
    - After your day input what you have done and the times that this has been done e.g. Gym 10am - 11am
    - Compare the days
    V2
    - Implement that when a previous activity is inputted into the program to take place that day, a suggested timeframe is shown 
    V3
    - ML implemented to suggest when certain activities should take place according to previous data
    V4
    - Input suggested activities for the day and day planner will put together a sample day with all events and take into account previous timeframes (+ fav times)
"""

def new_activity():
    activity = input("What's today's first activity? ")
    activity_starttime = input("What time are you planning to begin " + activity + "? ")
    activity_endtime = input("What time will " + activity + " end? ")

def view_day():    
    print("So far, your day looks like: " +  + "-" + activity_endtime + ": " + activity)

print("Welcome to Day Planner \n1. View your day \n2. Add activity \n3. Exit")
choice = input("Enter a number: ")
if choice == 1:
    view_day()
elif choice == 2:
    new_activity()
else:
    exit




todo_list = [
    {"activity": activity,
     "start_time": activity_starttime,
     "end_time": activity_endtime}
]

with open('todo_list.json', 'w') as file:
    json.dump(todo_list, file)

