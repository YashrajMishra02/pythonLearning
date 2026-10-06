# datetime
import datetime

dt = datetime.datetime(2025,12,12,2,12,20,20000) #predefined date and time

tnow = datetime.datetime.now()

tdelta = datetime.timedelta(days=7) # or tdelta = datetime.timedelta(hour=7)

print(dt)
print(tnow)
print(dt-tdelta)

# All methods of date and time applies here as well i.e

print(dt.day)
print(tnow.hour)
print(dt.year)
