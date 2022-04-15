
from datetime import datetime
"""
a = datetime(2019, 6, 29)
print(a)
first = datetime(2019,1,1)
print(first)

print(a-first)
print(f"{a} is the {(a-first).days+1}st day in {a.year}")
"""

def whichday(year, month, day):
    specified_date = datetime(year, month, day)
    first_day = datetime(year, 1, 1)
    return (specified_date - first_day).days + 1

print(whichday(2019, 6, 29))
