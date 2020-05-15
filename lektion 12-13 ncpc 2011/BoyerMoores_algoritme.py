
class PatternMatch:

    def __init__(self):
        super().__init__()

    def Boyer_Moores(self, T, P):
        if len(T) == 0 or len(P) == 0:
            return 0;
        last = len(P)-1
        for i in range(len(P)-1, len(T)-1):

            if P[last] == T[i]:
                tempP = last-1
                tempT = i -1
                while P[last] == T[i]:

                    if T[tempT] == P[tempP]:
                        if len(P)- tempP == len(P):
                            return tempT
                        else:    
                            tempP = tempP -1
                            tempT = tempT-1
                    else:
                        j =self._last(T[tempT], P)
                        tempT = tempT + len(P) - min(tempP  , j +1)
                        tempP = len(P) -1
        return -1




    #Tager et pattern P og det bogstav man leder efter p
    def _last(self, p, P: str):
        for i in range(len(P)-1, 1,-1):
            if p == P[i]:
                return i
        
        return -1

#print(Boyer_Moores.Boyer_Moores("abacaabadcabacabaabb", "abacab"))