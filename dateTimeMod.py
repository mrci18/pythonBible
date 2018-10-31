import datetime

x = datetime.datetime.now()
print(x)

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

#Unix epoch convert to datetime
y = datetime.datetime.fromtimestamp(1000000)
print(y)

#Time Delta
#Duration of time
# keyword arguments 
# weeks, days, hours, minutes, seconds, milliseconds, and microseconds.
delta = datetime.timedelta(days=10, hours=15, minutes=5, seconds=8)
print(delta.days, delta.microseconds, delta.seconds)
print("total_seconds() " + str(delta.total_seconds()))
print("Delta " + str(delta))

#Thousand days from today
today = datetime.datetime.now()
thousand_days = datetime.timedelta(days=1000)
print("Thousand days from today " + str((today + thousand_days)))

#Subtract timedelta
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print("Minus 30 years %s" % (oct21st - aboutThirtyYears))

#Pause until halloween2018
# halloween2018 = datetime.datetime(2018, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2018:
#     time.sleep(1)

#Format datetime objects into strings
oct22nd = datetime.datetime(2019, 10, 22, 16, 29, 0)
print(oct22nd.strftime('%Y/%m/%d %H:%M:%S'))
print(oct22nd.strftime('%I:%M %p'))
print(oct22nd.strftime('%B of %y'))

#Convert strings into datetime objects
#The p in the name of the strptime() function stands for parse
strp = datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(strp)
