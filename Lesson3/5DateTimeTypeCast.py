from datetime import datetime

# What if date is in string format like ?
dateTime_str = '2/15/2020 1:00:00 PM'
print(f"Actual representation before DateTiem formating = {dateTime_str}")
# Change the Data Type and format it
dateTime_obj = datetime.strptime(dateTime_str, '%m/%d/%Y %I:%M:%S %p')
print(f"Updated representation after DateTiem formating = {dateTime_obj}" )



