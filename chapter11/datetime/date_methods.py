# Methods of date
import datetime

tday = datetime.date.today()

print(tday.year)
print(tday.month)
print(tday.day)

# Methods for weekday
print(tday.weekday()) # monday == 0 ...... sunday == 6
print(tday.isoweekday()) # monday == 1 ...... sunday == 7