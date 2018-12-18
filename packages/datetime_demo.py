import datetime

# time
t = datetime.time(5, 25, 1)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(t.tzinfo)

print(datetime.time.max)
print(datetime.time.min)
print(datetime.time.resolution)


# date
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.timetuple())

print(datetime.date.max)
print(datetime.date.min)
print(datetime.date.resolution)

old_day = today.replace(year=1999)
print(old_day)

print('The diferrent in days between today and old_day are {}'.format(today - old_day))
