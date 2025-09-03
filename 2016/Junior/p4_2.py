startTimeString="23:20"
startMins=int(startTimeString.split(':')[0])*60 + int(startTimeString.split(':')[1])
startIndex = startMins//10 -1

#0:00 - 7:00
costList=[10]*21*2
#7:00 - 10:00 speed is half
costList=costList + [5]*9*2
#10:00 - 15:00 speed is normal
costList=costList + [10]*15*2
#15:00 - 19:00
costList=costList + [5]*12*2
#19:00 - 23:50
costList=costList + [10]*29

print(len(costList))
step=0
tripMins=120

weightedTrip=0
while True:
 
    
    weightedTrip = weightedTrip + costList[startIndex]
    #print(step,costList[startIndex],weightedTrip,startIndex)

    if weightedTrip == tripMins:
        #print(step,startIndex+1,((startIndex+1)*10)//60, ((startIndex+1)*10)%60)
        print("%02d:%2d" % (((startIndex+1)*10)//60, ((startIndex+1)*10)%60))
        break
    
    step = step + 1
    if (startIndex == 142):
        startIndex = 0
    else:
        startIndex = startIndex + 1
