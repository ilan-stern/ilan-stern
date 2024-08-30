import json
from datetime import datetime

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
todo_list = []

def get_time_input(prompt):
    while True:
        time_input = input(prompt)
        try:
            # Parse the time input, assuming a 24-hour format
            valid_time = datetime.strptime(time_input, "%H:%M")
            return valid_time.time()
        except ValueError:
            print("Invalid time format. Please enter the time in HH:MM format (24-hour). ")
            continue
    
def new_activity():
    # Gather details
    if not todo_list:
        activity = input("What's today's first activity? ")
    else:
        activity = input("What's another activity for today?")
    activity_starttime = get_time_input("What time are you planning to begin " + activity + "? (HH:MM) ")
    activity_endtime = get_time_input("What time will " + activity + " end? (HH:MM) ")

    # Add activity to todo_list
    todo_list.append({
        "activity": activity,
        "start_time": activity_starttime,
        "end_time": activity_endtime
    })

def view_day():
    if not todo_list:
        print("\nYour day is currently empty")
    else:
        print("So far, your day looks like:")
        for item in todo_list:
            start_time_str = item['start_time'].strftime("%H:%M")
            end_time_str = item['end_time'].strftime("%H:%M")
            print(f"{start_time_str} - {end_time_str}: {item['activity']}")

choice = 0
while choice != "3":
    print("\nWelcome to Day Planner \n1. View your day \n2. Add activity \n3. Exit")
    choice = input("Enter a number: ")
    if choice == "1":
        view_day()
    elif choice == "2":
        new_activity()
    else:
        exit



"""with open('todo_list.json', 'w') as file:
    json.dump(todo_list, file)
"""
