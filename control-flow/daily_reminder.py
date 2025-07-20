task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority: 
    case "high":
        if time_bound == "yes": 
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to address it soon.")
    case "medium": 
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to complete it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task tha still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider compleeiting it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
