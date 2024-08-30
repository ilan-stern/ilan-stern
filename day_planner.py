import json
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

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

def get_time_input(entry_widget):
    time_input = entry_widget.get()
    try:
        # Parse the time input, assuming a 24-hour format
        valid_time = datetime.strptime(time_input, "%H:%M")
        return valid_time.time()
    except ValueError:
        messagebox.showerror("Invalid time format. Please enter the time in HH:MM format (24-hour). ")
        return None
    
def new_activity():
    # Gather details
    activity = activity_entry.get()
    if not todo_list:
        if not activity:
            messagebox.showerror("Input error", "Please enter today's first activity")
            return
    else:
        if not activity:
            messagebox.showerror("Input Error", "Please enter another activity for today.")
            return

    activity_starttime = get_time_input(start_time_entry)
    activity_endtime = get_time_input(end_time_entry)

    if activity and activity_starttime and activity_endtime:
        
    # Add activity to todo_list
        todo_list.append({
            "activity": activity,
            "start_time": activity_starttime,
            "end_time": activity_endtime
        })
        update_day_view()
        clear_entries()

def view_day():
    if not todo_list:
        messagebox.showinfo("Day Planner", "Your day is currently empty!")
    else:
        update_day_view()
        

def update_day_view():
    day_view.delete(1.0, tk.END)
    if not todo_list:
        day_view.insert(tk.END, "Your day is currently empty\n")
    else:
        for item in todo_list:
            start_time_str = item['start_time'].strftime("%H:%M")
            end_time_str = item['end_time'].strftime("%H:%M")
            day_view.insert(tk.END, f"{start_time_str} - {end_time_str}: {item['activity']}\n")


def clear_entries():
    activity_entry.delete(0, tk.END)
    start_time_entry.delete(0, tk.END)
    end_time_entry.delete(0, tk.END)

# Initialise the main window
root = tk.Tk()
root.title("Day Planner")

# Activity input
activity_label_text = tk.StringVar()
activity_label_text.set("What's today's first activity? ")
activity_label = tk.Label(root, textvariable=activity_label_text)
activity_label.grid(row=0, column=0, padx=0, pady=5)

activity_entry = tk.Entry(root)
activity_entry.grid(row=0, column=1, padx=10, pady=5)

# Start time input
tk.Label(root, text="Start Time (HH:MM):").grid(row=1, column=0, padx=10, pady=5)
start_time_entry = tk.Entry(root)
start_time_entry.grid(row=1, column=1, padx=10, pady=5)

# End time input
tk.Label(root, text="End Time (HH:MM):").grid(row=2, column=0, padx=10, pady=5)
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=2, column=1, padx=10, pady=5)

# Add Activity button
add_button = tk.Button(root, text="Add Activity", command=new_activity)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# View Day button
view_button = tk.Button(root, text="View Day", command=view_day)
view_button.grid(row=4, column=0, columnspan=2, pady=5)

# Day view
day_view = tk.Text(root, height=10, width=40)
day_view.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=6, column=0, columnspan=2, pady=5)

# Start the main loop
root.mainloop()

"""
while choice != "3":
    print("\nWelcome to Day Planner \n1. View your day \n2. Add activity \n3. Exit")
    choice = input("Enter a number: ")
    if choice == "1":
        view_day()
    elif choice == "2":
        new_activity()
    elif choice == "3":
        print("Exiting Day Planner. Have a great day!")
    else:
        print("Invalid choice, pleas enter 1, 2, or 3.")
"""


"""with open('todo_list.json', 'w') as file:
    json.dump(todo_list, file)
"""


"""print("\nSo far, your day looks like:\n")
        for item in todo_list:
            start_time_str = item['start_time'].strftime("%H:%M")
            end_time_str = item['end_time'].strftime("%H:%M")
            print(f"{start_time_str} - {end_time_str}: {item['activity']}")
"""