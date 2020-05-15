


def club(maxDif, Q):
    actualDif = 0
    numMen = 0
    numWomen = 0
    popped = []

    while (len(Q) > 1):
        next = 0
        while(actualDif <= maxDif and len(Q) > 0):
            #En for meget bliver tilføjet tilsidst
            next = Q.pop(0)
            if next == 'M':
                numMen += 1
            else:
                numWomen += 1
            
            popped.append(next)

            if(numMen > 0 and numWomen > 0):
                actualDif = abs(numMen - numWomen)
        
        if (len(Q) > 0):
            
            next = Q.pop(0)

            #En for meget bliver tilføjet til sidst
            if next == 'M':
                if actualDif > abs(((numMen +1) - numWomen)):
                    numMen += 1
                    popped.append(next)
            
            else:
                if actualDif > abs(numMen - (numWomen +1)):
                    numWomen += 1
                    popped.append(next)
            
            if(numMen > 0 and numWomen > 0):
                actualDif = abs((numMen - numWomen))
            
            if(actualDif > maxDif):
                return numMen + numWomen-1
    return numMen + numWomen




print(club(1, ['M', 'W','W','M','W','M','M','W','M']))
print(club(2, ['W', 'M','M','M','M','W','W','M','M', 'M', 'W', 'M', 'W']))
print(club(2, ['W', 'M','W','M','M','W', 'M','W','M','M', 'M', 'W', 'M', 'W']))


