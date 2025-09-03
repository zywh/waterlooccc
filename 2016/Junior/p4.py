
from datetime import datetime,date,time,timedelta

startString="06:20"
fmt = '%H:%M'
startTime = datetime.strptime(startString, fmt) #datatime object
startHour = startTime.hour

print(startHour)

if (startHour <= 5) or (startHour <=13 and startHour >=10 ) or (startHour >=19):
    arriveTime = startTime + timedelta(hours=2)
    print(arriveTime.strftime("%H:%M"))
elif (startHour > 5 and startHour <=7):
    
    firstSeg = datetime.strptime('07:00',fmt) - startTime
    leftMins = 120 - firstSeg.seconds/60
    if ( leftMins < 90):  # 90*2 = 180 mins between 7 and 10
        #between 7 and 10
        t = leftMins*2
        arriveTime = datetime.strptime('07:00',fmt) + timedelta(minutes=t) 
    else:
        #Beyond 10
        arriveTime = startTime + timedelta(minutes=180) + timedelta(minutes=(leftMins - 90))    

    print("5-7 start or 13-15 start", arriveTime.strftime("%H:%M"))
else:
    print("coming")
   