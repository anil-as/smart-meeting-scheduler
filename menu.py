import datetime
from scheduler import Scheduler

def main():
    scheduler = Scheduler(holidays=[datetime.date(2025, 4, 18), datetime.date(2025, 12, 25)])

    while True:
        print("\nSmart Meeting Scheduler")
        print("1. Schedule a Meeting")
        print("2. Check Available Time Slots")
        print("3. View Scheduled Meetings")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            user = input("Enter your name: ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            start_hour = int(input("Enter start hour (24-hour format): "))
            end_hour = int(input("Enter end hour (24-hour format): "))
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            print(scheduler.schedule_meeting(user, date, start_hour, end_hour))

        elif choice == "2":
            user = input("Enter your name: ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            slots = scheduler.get_available_slots(user, date)
            print("Available slots:", slots if slots else "No available slots.")

        elif choice == "3":
            user = input("Enter your name: ")
            meetings = scheduler.view_meetings(user)
            print("Your scheduled meetings:", meetings if meetings else "No meetings scheduled.")

        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")
