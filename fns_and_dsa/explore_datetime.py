#explore_datetime.py

from datetime import datetime, date, time, timedelta

def display_current_datetime():
    #Get the current date and time
    current_date = datetime.now()
    #Format the date and time into a readable string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    #print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user to enter a number of days and calculates the future date
    after adding those days to the current date.
    """
    try:
        #Prompt the user to enter the number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date"))
    except ValueError:
        # Handle the case where the user input is not a valid integer
        print("Invalid input. Please enter an integer")
        return
current_date = datetime.now()

future_date = current_date + timedelta(days=days_to_add)

formatted_future_date = future_date.strftime("%Y-%m-%d")

print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()

    calculate_future_date()
