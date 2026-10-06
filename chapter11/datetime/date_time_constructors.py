# datetime consturctors
import datetime

dt_today = datetime.datetime.today() # is not timezone aware

dt_now = datetime.datetime.now() # timezone is set to null

dt_utcnow = datetime.datetime.utcnow() # function has been dropped 

print(dt_today)
print(dt_now)
print(dt_utcnow)
