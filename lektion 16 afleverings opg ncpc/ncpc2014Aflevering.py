def D_2014(Gunnars_dice, Emmas_dice):
    sumGunnar = 0
    sumEmma = 0
    for i in Gunnars_dice:
        sumGunnar += i
    
    for i in Emmas_dice:
        sumEmma += i
    
    if sumEmma > sumGunnar:
        return "Emma"
    if sumGunnar > sumEmma:
        return "Gunnar"
    else:
        return "Tie"


def G_2014(n, k, x):
    canJoin = 0
    
    def find(arr, index, potentiallyJoin, canJoin):
        par = arr[index]
        arr[index] = 0
        potentiallyJoin += 1

        if arr[par-1] == par or arr[par-1] == 0:
            
            canJoin += potentiallyJoin
            potentiallyJoin = 0
            if canJoin <=k:
                return canJoin
            else:
                return 0
        else:
            return find(arr, par-1, potentiallyJoin, canJoin)
            
    for i in range(n):
        canJoin = max(find(x.copy(), i, 0, canJoin), canJoin)
    
    return canJoin

def I_2014(n, lines):

    totalSquares = 0
    
    #Sortere linjerne i forhold til deres hældning
    def sort(vandret, lodret, neg, pos, lines):       
        if(len(lines)> 0):
            koor = lines[0]
            try:
                #hældningskoefficienten
                #En lodret linje har ingen hældningskoefficent og giver derfor en fejl
                a = (koor[3] - koor[1]) / (koor[2] - koor[0])
            except ArithmeticError as e:
                lodret.append(koor)
            else:
                if(a == 0):
                    vandret.append(koor)
                elif(a <0):
                    neg.append(koor)
                else:
                    pos.append(koor)
            
            return sort(vandret, lodret, neg, pos, lines[1:])
        else:
            return (vandret, lodret, neg, pos)
    
    slines = sort([], [], [], [], lines)



    #Finder antal gange hvor længden mellem 2 linjer er lig med target
    # xOrY = 1 | 0: i forhold til retningen af linjen skal man sammenligne på x og på y
    # targetLine: bestemmer hvilken linje man kigger på
    #count: tæller hvor mange gange et bestemt mellemrum findes
    def findDis(dir, target, count, xOrY, targetLine):

        if(len(dir)> targetLine):
            
            #udregner afstanden mellem 2 linjer
            dis = abs(dir[0][xOrY]-dir[targetLine][xOrY])

            if(dis == target):
                count +=1
                targetLine = 1
            elif (dis < target):

                #Tjekker at punkterne som ligger parallelt for hinnanden bliver sammenlignet
                if(abs(dir[0][xOrY]-dir[targetLine][xOrY+2])== target):
                    count +=1
                    targetLine = 1
                else:
                    return findDis(dir, target, count,xOrY, targetLine+1)
            else:
                return findDis(dir, target, count, xOrY, targetLine-1)

            return findDis(dir[1:], target, count, xOrY, targetLine)
        else:
            return count

    def match(dir, opDir, xOrY, balance):
        subSquares = 0

        for i in range(1,min(len(dir), len(opDir))):
            countA = findDis(dir.copy(), i, 0, xOrY, 1)
            countB = findDis(opDir.copy(), i, 0, xOrY-balance, 1)

            subSquares += countA*countB
    
        return subSquares

    #tjekker kvadrater dannet af de vandrete og lodrete linjer
    totalSquares += match(slines[0], slines[1],1,1)
    
    #tjekker kvadeater dannet af de negative og positive linjer 
    totalSquares += match(slines[2], slines[3], 1, 0)
    
    return totalSquares
