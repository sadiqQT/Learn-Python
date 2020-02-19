#TimeDelta is useful for calculting difference in DateTime
# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

from datetime import timedelta

# roughly assume that month has 30 
monthly = timedelta(days=30)
# roughly quarter has 90 days
quaterly = timedelta(days=90)

# How many days in a year ?
yearly = quaterly * 4
print(f"Roughly number of days in a year is {yearly}")

# How many days in 2 quaters using monthly variable ?
twoQuaters = monthly * 6
print(f"Number of days in a year is {twoQuaters}")

# How many days in 2 quaters using quaterly variable ?
twoQuaters = quaterly * 2
print(f"Number of days in a year is {twoQuaters}")
