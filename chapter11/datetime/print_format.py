import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz = pytz.UTC)

# Printing the date time in international format using isoformal
dt_mine = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))

print(dt_mine.isoformat())

# strftime: Convert Datetime to string
print(dt_mine.strftime('%B %d, %Y'))

# strptime: Convert String to Datetime
dt_str = 'September 28, 2026'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

