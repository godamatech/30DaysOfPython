# Python Date time
# Exercises: Day 16

from datetime import datetime
from datetime import date as d

now = datetime.now()

day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
timestamp=now.timestamp

print("Current Day: ",day)
print("Current Month: ",month)
print("Current Year: ",year)
print("Current Hour: ",hour)
print("Current Minute: ",minute)
print("Current Timestamp: ",timestamp())

print()

# 3

# 4

todays_date = d(day=day, month=month, year=year)
new_year = d(day=1, month=1, year=year+1)
# current = d(day=day, month=month, year=year)
time_remain = new_year - todays_date

print(f"Time remaining to New Year: {time_remain}")
print()


given_date = d(day=1, month=1, year=1970)
current = d(day=day, month=month, year=year)
diff = current - given_date

print(f"The diffirence between the given date and the current date is: {diff}")
print()

print("datetime module can be used in many use case in a program such as:\n\t - to determine birthdays of people.\n\t - to keep time rocord of when something was created/modified.  ")
print()



# print(f'{day}/{month}/{year}, {hour}:{minute}')

# formated_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("Formated date and time : ",formated_time)

# print(now.strftime("%H:%M:%S %p"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))
# print(now.strftime("%c"))
# print(now.strftime("%a, %b %d"))

# a=d(2023,4,4)
# b=d(1999,4,4)
# print(f"I am {a - b} years old.")

# print(datetime(2024,2,29))
# print(datetime.now().date())

