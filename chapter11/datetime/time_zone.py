import datetime
import pytz

dt = datetime.datetime(2024, 6, 15, 12, 2, 34, 100000, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
print(f"UTC Time: {dt_utcnow}")

# Convertion dt_utcnow timezone into different my_timezone
dt_mine = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(f"Local Time(with timeaware): {dt_mine}")

# Printing all the timezones
for item in pytz.all_timezones:
    print(item) 

# Converting Naive time into timezone aware
dt_mine = datetime.datetime.now()
print(f"Local Time(without timeaware): {dt_mine}")

# Creating local timezone function
mine_tz = pytz.timezone('Asia/Kolkata')

# now as we have localize timezone we update the naive timezone with our local time
dt_mine = mine_tz.localize(dt_mine)

tokyo_tz = dt_mine.astimezone(pytz.timezone('Asia/Tokyo')) # this cause error because our dt_mine doesn't have time zone and (astimezone cannot be applied to a naive datetime)

print(f"Tokyo Time: {tokyo_tz}") 

