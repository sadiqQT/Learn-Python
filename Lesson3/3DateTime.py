# to import any library in Python
# one needs to write like
# from *** import ***
# for example
# from datetime import datetime

from datetime import datetime
# print Date and Time
print(datetime.now())
#Make it more readable 
print(f"What is the Date and Time now ? = {datetime.now()} " )
# Print individual info.
print(f"Today's Day  ? = {datetime.now().day} " )
print(f"Today's Month  ? = {datetime.now().month} " )
# Can you print current year ?
print(f"Today's Year  ? = {datetime.now().year} " )
