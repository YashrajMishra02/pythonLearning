# Import datetime module
import datetime

# Naive datetime approach
d = datetime.date(2025, 9,2)
print(d)

# Error while writing date,month with Leading ZERO cause SyntaxError
d = datetime.date(2026, 09,28)
print(d)

# Constructing today's date
tday = datetime.date.today()
print(tday)