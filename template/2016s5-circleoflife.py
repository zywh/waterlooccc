def newState(before,after):
    if  int(before) + int(after) == 1:
    # if ( before == 1 and after == 0) or (before ==0 and after == 1)
        return '1'
    else:
        return '0'

t=3
state='01011'

for r in range(t):
    newS=''
    for i in range(len(state)):
        before=state[i-1]
        if i == len(state) - 1:
            after=state[0]
        else:
            after=state[i+1]  
        y = newState(before,after)     
        newS = newS + y

    state=newS
print(state)