from sys import stdin
#Read Input Function

def readInput():
    inputList=[]
    for line in stdin:
        inputList.append(line.strip())
    return inputList
  

vInput=readInput()
n = vInput.count('W')
#vInput=['W','W','L','W']
if ( n >=5 ):
    print(1)
elif (n >= 3):
    print(2)
elif ( n >= 1):
    print(3)
else:
    print(-1)    
   
