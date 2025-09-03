
#Import
from sys import stdin
#import math


#Read Input Function

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList    

#Call readInput function and return result to vInput variable

#Debug Sample2

#vInput=['16 3 2 13','5 10 11 8','9 6 7 12','4 15 14 2']
vInput=['16 3 2 13','5 10 11 8','9 6 7 12','4 15 14 1']
#
vInput=[x.split() for x in vInput]

#Start Main Program
vResult=True
vSum=int(vInput[0][0]) +int(vInput[0][1]) +int(vInput[0][2]) +int(vInput[0][3])
print("Base:",vSum)


for x in range(4):
  vRowSum,vColSum=0,0
  for y in range(4):
    #print(x,y,vInput[x][y],vInput[y][x])
    vRowSum = vRowSum + int(vInput[x][y])
    vColSum = vColSum + int(vInput[y][x])
    
  #print("Row/Col Result:",vRowSum,vColSum)  
  if vRowSum != vSum or vColSum != vSum:
      vResult=False
      break


      
      

if vResult:
  print("Magic")
else:
  print("No Magic")
