# Learning of timeDeltas used to know the duration between two date or time
import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)

# print(tday + tdelta) # shows what the date would be 7 days after
# print(tday - tdelta) # shows what the date would be 7 days before

bday = datetime.date(2026,12,2)

time_delta_bday = bday - tday

print(time_delta_bday) # By default shows date and time 

# print(time_delta_bday.days) # Shows only days
print(time_delta_bday.total_seconds()) 

