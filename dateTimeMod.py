import datetime

x = datetime.datetime.now()
print(x)

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

#Unix epoch convert to datetime
y = datetime.datetime.fromtimestamp(1000000)
print(y)