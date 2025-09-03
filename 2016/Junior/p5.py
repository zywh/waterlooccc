vInput=['1','3','5 1 4','6 2 4']
vInput=['2','3','5 1 4','6 2 4']
#vInput=['2','5','202 177 189 589 102','17 78 1 496 540']

vQuestion=vInput[0]
vCount = int(vInput[1])
vList1 = [int(x) for x in vInput[2].split()]
vList2 = [int(x) for x in vInput[3].split()]

vList1.sort()
if ( vQuestion == '1'):
    vList2.sort()
else:
    vList2.sort(reverse=True)
print(vList1,vList2)
totalSpeed=0
for i in range(vCount):
    
    totalSpeed = totalSpeed + max(vList2[i],vList1[i])
    print("pair:",max(vList2[i],vList1[i]),totalSpeed)