def elevatorTruble(floors, start, goal, up, down):
    
    #vi har floors +1 fordi så behøver man ikke tænke over
    # at skulle trække en fra når man skal give input
    building = [-1] * (floors +1)
    building[start] = 0
    l = [start]

    while len(l) > 0:

        #current er index
        current = l.pop(0)
        low = current - down
        heigh = current + up

        if low >= 1  and  building[low]== -1:   
            l.append(low)
            building[low] = building[current] +1
            
            if low == goal:
                return building[low]
        
        if  heigh < len(building) and building[heigh]== -1 :
            l.append(heigh)
            building[heigh] = building[current] +1

            if heigh == goal:
                return building[heigh]
    
    return "use the stairs"

print(elevatorTruble(100, 2, 1, 1, 0))