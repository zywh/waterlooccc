
from sys import stdin

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList   


#vInput = readInput()
vInput='abracadabra'
vInputRev=vInput[::-1]

maxLen=1
#list(range(len(vInputRev),0,-1))

for i in range(len(vInput)):
    for j in range(len(vInput),0,-1):
      vStr=vInput[i:j]
      #print(vStr,vInputRev)
      if vInputRev.find(vStr) >= 0:
        maxLenNew=len(vStr)
        print("Find Matching:",vStr,len(vStr))
        if ( maxLenNew > maxLen):
          maxLen = maxLenNew


print(maxLen) 
  