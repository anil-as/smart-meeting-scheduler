import datetime

class Scheduler:
    def __init__(self, working_hours=(9, 17), holidays=None):
        """Initialize the scheduler with working hours and holidays."""
        self.working_hours = working_hours  
        self.holidays = holidays if holidays else []  
        self.schedule = {}  
    
    def is_working_day(self, date):
        return date.weekday() < 5 and date not in self.holidays

    def get_available_slots(self, user, date):
        if not self.is_working_day(date):
            return []
        booked_slots = self.schedule.get(user, {}).get(date, [])
        available_slots = [(hour, hour+1) for hour in range(self.working_hours[0], self.working_hours[1])]
        return [slot for slot in available_slots if slot not in booked_slots]

    def schedule_meeting(self, user, date, start_hour, end_hour):
        if not self.is_working_day(date):
            return "Cannot schedule on weekends or holidays."
        if start_hour < self.working_hours[0] or end_hour > self.working_hours[1]:
            return "Meeting time must be within working hours."
        if start_hour >= end_hour:
            return "Invalid time slot."
        
        user_meetings = self.schedule.setdefault(user, {}).setdefault(date, [])
        for (s, e) in user_meetings:
            if not (end_hour <= s or start_hour >= e):
                return "Time slot overlaps with an existing meeting."
        
        user_meetings.append((start_hour, end_hour))
        return "Meeting scheduled successfully."

    def view_meetings(self, user):
        return self.schedule.get(user, {})
