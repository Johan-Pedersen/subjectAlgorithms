
competingMoose1 = [(2011, 1), (2011, 3), (2014, 4),(2012, 6)] #Result == 2013
competingMoose2 = [(2013, 2), (2012, 4), (2011, 5),(2014, 3)] #Result == unknown 

def kingOfTheForest(size, years, karlYear, karlStrength, arrayOfMosse):
    
    canWin = True
    if karlYear <= 2011+years:
        for m in arrayOfMosse:
            if karlYear == m[0]:
                if(karlStrength < m[1]):
                    canWin = False
    
    if canWin:
        return karlYear
    else:
        return "unknown"


print(kingOfTheForest(2,4,2013, 2, competingMoose1))
print(kingOfTheForest(2,4,2011, 1, competingMoose2))