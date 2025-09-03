from datetime import datetime,date,time,timedelta

vDatetime1 = datetime(2017,10,8,10,56)
vDatetime2 = datetime(2017,12,8,11,56)
#Format1
fmt1 = '%Y-%m-%d %H:%M:%S'
dateString1 = '2010-01-01 17:31:22'
#Another format
fmt2 = '%Y/%m/%d %H-%M-%S'
dateString2 = '2012/01/11 18-31-22'
#Convert to datetime object
vDatetime3 = datetime.strptime(dateString1, fmt1) 
vDatetime4 = datetime.strptime(dateString2, fmt2) 

#Convert datetime to string using fmt1
vDatetime3String = vDatetime3.strftime(fmt1)

# Time diff
timeDiff1 = vDatetime4 - vDatetime3
timeDiff2 = timedelta(days=1,hours=2,minutes=10)


print(timeDiff1.days)
print(timeDiff2.seconds)


vDate = date(2017,12,8)
vTime = time(10,11)
vTime2 = time(12)
s = vTime2.minute

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print((vDatetime4-vDatetime3).seconds + (vDatetime4-vDatetime3).days*24*3600)  #output 867600
print(vDatetime3 + timeDiff1) # output 2010-01-02 19:41:22

print(vDatetime4.timestamp()-vDatetime3.timestamp()) # output 867600.0

#4 January Jan Friday Jan PM
print(vDatetime3.weekday() , vDatetime3.strftime("%B"),vDatetime3.strftime("%b"),vDatetime3.strftime("%A"),vDatetime3.strftime("%b"),vDatetime3.strftime("%p")) 

# Output 2010 1 1 17 31 22
print(vDatetime3.year,vDatetime3.month,vDatetime3.day,vDatetime3.hour,vDatetime3.minute,vDatetime3.second) 
#2010 10 01 31 17 00
print(vDatetime3.strftime("%Y"),vDatetime3.strftime("%y"),vDatetime3.strftime("%m"),vDatetime3.strftime("%M"),vDatetime3.strftime("%H"),vDatetime3.strftime("%W"))

print(vDatetime3.timetuple())  #time.struct_time(tm_year=2010, tm_mon=1, tm_mday=1, tm_hour=17, tm_min=31, tm_sec=22, tm_wday=4, tm_yday=1, tm_isdst=-1)
print(vDatetime3.timetuple().tm_hour)  # output 17


